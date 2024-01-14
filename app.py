from flask import Flask, render_template, request, redirect, abort
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Vishal@1234',
    'database': 'flaskdb'
}

@app.route("/")
def mainPage():
    return "This is my Flask project"

@app.route("/hello")
def return_hello():
    return "Hello World"

@app.route('/users')
def users():
    try:
        # Connect to MySQL
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Fetch users from the database
        cursor.execute("SELECT id, name, email, password, role FROM new_table")
        users_data = cursor.fetchall()

        # Close MySQL connection
        cursor.close()
        connection.close()

        # Render the HTML template with the user data
        return render_template('users.html', users=users_data)

    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/new_user')
def new_user():
    return render_template('new_user.html')

@app.route('/create_user', methods=['POST'])
def create_user():
    try:
        # Connect to MySQL
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Get user input from the form
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']

        # Insert user into the database, excluding the 'id' column
        insert_query = "INSERT INTO new_table (name, email, password, role) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (name, email, password, role))

        # Commit changes and close MySQL connection
        connection.commit()

        # Fetch the last inserted id
        last_inserted_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return redirect('/users')  # Redirect to the user list after creating a new user

    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/users/<int:user_id>')
def get_user(user_id):
    try:
        # Connect to MySQL
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Fetch the user from the database
        cursor.execute("SELECT id, name, email, password, role FROM new_table WHERE id = %s", (user_id,))
        user_data = cursor.fetchone()

        # Close MySQL connection
        cursor.close()
        connection.close()

        if user_data:
            # Render the HTML template with the user data
            return render_template('user_detail.html', user=user_data)
        else:
            # User not found, return a 404 error
            abort(404)

    except Exception as e:
        # Handle other exceptions
        return f"An error occurred: {str(e)}", 500

app.static_folder = 'static'    


if __name__ == '__main__':
    app.run(debug=True)

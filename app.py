from flask import Flask, render_template, request, redirect
import db_collection as dbc
from db_config import get_database


app = Flask(__name__)


database = get_database()

collection   = database[dbc.USER_COLLECTION]


# Home route - Displays a form and user data
@app.route('/')
def index():
    
    return render_template('index.html')


# Route to add a user
@app.route('/add_user', methods=['POST'])
def add_user():
    # Get form data
    name = request.form.get('name')
    age = request.form.get('age')
    city = request.form.get('city')

    # Create the user document to insert into MongoDB
    user = {
        "name": name,
        "age": int(age),
        "city": city
    }

    # Insert the user into the collection
    collection.insert_one(user)

    return redirect('/')  # Redirect back to home page


if __name__ == "__main__":
    app.run(debug=True)


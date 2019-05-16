from flask import render_template, request, flash, redirect, url_for
from application import app
from application.auth.auth import Authenticator


@app.route('/index', methods=['GET'])
def index():
    """ This method will display the index page """
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # GET request
    # Display the login form, where username and password can be entered
    if request.method == 'GET':
        return render_template('login.html')

    # POST request
    # Check if the input username and password are valid
    # If yes redirect to index page else display error message
    username = request.form['username']
    password = request.form['password']
    if Authenticator.is_valid(username, password):
        flash('Login successful !!')
        return redirect(url_for('index'))

    flash('Invalid username or password !!')
    return redirect(url_for('login'))

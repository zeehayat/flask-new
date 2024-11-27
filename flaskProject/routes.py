from flask import render_template, flash, redirect

from app import app
from form import LoginForm


@app.route('/')
def hello_world():  # put application's code here
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)

@app.route('/test')
def test():
    return 'Hello Test World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        flash('Login request for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/')
    return render_template('login.html', title='Home', form=form)
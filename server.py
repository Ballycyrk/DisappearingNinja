from flask import Flask, session, flash, render_template, request, redirect
app=Flask(__name__)
app.secret_key="pigsinablanket"
@app.route('/')
def index():
  return render_template('index.html')
@app.route('/users/,username.')
def show_user_profile(username):
  return render_template('index.html', username=username)
app.run(debug=True)

from flask import Flask, session, flash, render_template, request, redirect
app=Flask(__name__)
app.secret_key="pigsinablanket"
@app.route('/')
def index():
  return render_template('index.html')
@app.route('/ninja')
def groupHug():
  return render_template('ninja.html')
@app.route('/ninja/<color>')
def show_ninja(color):
  request = ('blue','orange','red','purple')
  for i in request:
    print color, i
    if i == color:
      break
    elif i == 'purple':
      color = 'megan_fox'
  return render_template('ninja.html', color=color)
app.run(debug=True)

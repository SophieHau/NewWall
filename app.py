from flask import Flask, render_template, request, redirect, url_for
from message import Message
from user import User

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
  message = Message()

  if request.method == 'POST':
    message.save('frankSinatra', request.form['message-text'])

  # message.close()

  return render_template('index.html', messages=message.all())

@app.route('/signup/', methods=['POST', 'GET'])
def signup():
    u = User()
    if request.method == 'POST':
        u.add_user(request.form.get('new_username'), request.form.get('new_password'))
        return redirect(url_for('index'))
    return render_template('signup.html')

@app.route('/login/', methods=['POST', 'GET'])
def login():
    u = User()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if u.get_user(username, password) == True:
            return redirect(url_for('index'))
        else:
            return render_template('signup.html')
    return render_template('login.html')
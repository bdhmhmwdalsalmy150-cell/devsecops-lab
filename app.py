import os
import sqlite3
from flask import Flask, request
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', os.urandom(24))
csrf = CSRFProtect(app)

@app.route('/user')
def get_user():
    username = request.args.get('username')
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        return str(cursor.fetchall())

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

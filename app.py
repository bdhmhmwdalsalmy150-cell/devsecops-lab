import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route('/user')
def get_user():
    username = request.args.get('username')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # ثغرة متعمدة: SQL Injection
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return str(cursor.fetchall())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, request
import sqlite3

app = Flask(__name__)

# Connect to a sample database (for demonstration purposes)
def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn

# Vulnerable route (SQL Injection risk)
@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    # ⚠️ Insecure SQL query (prone to SQL Injection)
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query)  # 🚨 Directly executing user input!
    users = cur.fetchall()
    conn.close()

    return f"User(s) Found: {users}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

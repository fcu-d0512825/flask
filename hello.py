import sqlite3
from flask import Flask,render_template,g
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello, World!!</h1>"
if __name__ == "__main__":
    app.run(debug=True)
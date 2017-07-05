from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<a href='https://www.google.com'>Hello, HTML!</a>"

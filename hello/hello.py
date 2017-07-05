from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g, flash

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('hello.html')

from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def index():
    return "index page"


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/call_rpc")
def call_rpc():
    pass

@app.route("/send_msg")
def send_msg():
    pass

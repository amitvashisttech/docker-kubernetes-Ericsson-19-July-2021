# Basic Flask App.
from flask import Flask, render_template
import os 
import socket

app = Flask(__name__)

@app.route("/")
def home():
     return "Welcome to Basic Flask App"

@app.route("/hello")
def hello_world():
     return "hello world"

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name


@app.route("/info")
def hello_page():
    html="<h2>Welcome to Docker & Python based WebServer</h2>"\
         "<b>Hostname: {hostname}</b>"
    return html.format(hostname=socket.gethostname())


if __name__ == '__main__':
   app.run('0.0.0.0',80)

__author__ = 'rudy'

from flask import Flask

#create the application object:
app = Flask(__name__)

#Use decorators to link to an URL:
@app.route("/")
@app.route("/hello")

#define the view using a function, wich returns a string:
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()


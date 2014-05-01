__author__ = 'rudy'

from flask import Flask

#create the application object:
app = Flask(__name__)

#Error handling:
app.config["DEBUG"]= True

#Use decorators to link to an URL:
#Static routes:
@app.route("/")
@app.route("/hello")

#define the view using a function, wich returns a string:
def hello_world():
    return "Hello, World!"

#Dynamic routes:
@app.route("/test/<search_query>")
def search(search_query):
    return ("Test search:" + search_query)


if __name__ == "__main__":
    app.run()


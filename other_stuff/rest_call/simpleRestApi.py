# importing the Flask from flask
from flask import Flask

app = Flask(__name__)

# the route() takes a path
# if route("/") then the default path(127.0.0.1:5000) is the method under it
# if route("/some_path") then 127.0.0.1:5000/some_path get the content from the method


@app.route("/")
@app.route("/hello")
def hello():
    return "Welcome to programming"

# the app.run makes the flask start when this file is called


if __name__ == '__main__':
    app.run(debug=True)

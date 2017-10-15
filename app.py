# coding:utf8
# for test
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1 style='color:red'>hello app</h1>";

if __name__ == "__main__":
    app.run()

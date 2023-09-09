from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/Name")
def Name():
    return "<h1>Md Ayan Arshad</h1>"

@app.route("/College")
def College():
    return "<h1>IITM</h1>"

@app.route("/test")
def test():
    a = 5 + 5
    return "this is my test function {}".format(a)

@app.route("/test2/test2")
def test2():
    data = request.args.get("x")
    return "This is my data input from my URL {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")

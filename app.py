from flask import Flask

app=Flask(__name__)
@app.route("/")
def index():
    return "hello...."
@app.route("/home")
def home():
    return "my home"
@app.route("/condact")
def condact():
    return "84985955"
if(__name__=="__main__"):
     app.run()

from flask import Flask, redirect, url_for

app = Flask(__name__)

#esempio
@app.route("/home")
def home():
    return "Hello Word!"

#parametro
@app.route("/<name>") # <nomeparam>
def user(name):
    return f"Hello: {name}"

#redirect
@app.route("/admin")
def admin():
    return redirect(url_for("home"))    #url_for -> nome funz e non path

#redirect con args
@app.route("/newusr")
def newusr():
    return redirect(url_for("user", name="valore"))    #funz, nomeattr=valore

#parametro
@app.route("/<v1>/<v2>") # <nomeparam>
def two_args(v1, v2):
    return f"V1: {v1} V2: {v2}"

#redirect con args
@app.route("/twoval")
def redirtwoargs():
    return redirect(url_for("two_args", v1="val1", v2="val2"))    #funz, nomeattr=valore

if __name__ == "__main__":
    app.run()
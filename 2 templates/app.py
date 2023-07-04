from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

#esempio
@app.route("/debug")
def debug():
    return "debug"

# template
@app.route("/")
def home():
    return render_template("index.html")

# dinamic info
@app.route("/<name>")
def hello(name):
    return render_template("hello.html", content=name, val=3)

#pass lista
@app.route("/list")
def list():
    return render_template("list.html", genres =['horror','love','action'])

# template fuori folder templates
'''@app.route("/notemp")
def home_no_templates():
    return render_template("../nontemplates/index.html")
'''

if __name__ == "__main__":
    app.run(debug=True)
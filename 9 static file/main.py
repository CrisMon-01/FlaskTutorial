from flask import Flask, render_template

app = Flask(__name__)

@app.route("/debug")
def debug():
    return "DEBUG!" 

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)

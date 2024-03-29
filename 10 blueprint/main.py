from flask import Flask, render_template
from second import second

app = Flask(__name__)
# app.register_blueprint(second, url_prefix="") #con uguale path vince second, e non app nella selez. degli url
app.register_blueprint(second, url_prefix="/admin") 

@app.route("/debug")
def debug():
    return "DEBUG!" 

@app.route("/") # vado a / di second
def home():
    return "<h1>Test</h1>"

if __name__ == "__main__":
    app.run(debug=True)

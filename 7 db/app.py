from flask import Flask, redirect, url_for, render_template, request, session, flash
#sqlalchemy db
import sqlalchemy

# gestione permanenza sessioe, fino a permanent session
from datetime import timedelta

app = Flask(__name__)
# prima di tutto secret_key è come decifro i dati della sessione (cifrati)
# per ora una cosa qualsias8i
app.secret_key="aaa"
#gestione permanenza e durata sessione
app.permanent_session_lifetime = timedelta(seconds=10)

#esempio
@app.route("/debug")
def debug():
    return "debug"

# template
@app.route("/")
def home():
    return render_template("index.html")

# template
@app.route("/login", methods=["POST","GET"])
def login():
    if request.method=="POST":
        #rendo da qui sessione permanente, default = False per non permanent
        session.permanent = True
        user = request.form['nm'] #request.form['nomecampo']
        #metto/SETTO la sessione
        session['user'] = user #<k,v>
        #db

        flash(f"{user} logged In!", "info")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash(f"Already logged in!", "info")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user", methods=['POST', 'GET'])
def user():
    #DB POST O GET
    email = None

    #prendo sessione
    if "user" in session:
        user = session['user']

        if request.method=='POST':
            email = request.form['email']
            session['email'] = email
        else:
            if 'email' in session:  
                email = session['email']
        return render_template("user.html", email=email)
    else:
        flash(f"You had to login", "info")
        return redirect(url_for("login"))
    
# clear session
@app.route("/logout")
def logout():
    if "user" in session:
        user = session['user']
        flash(f"{user} logged out!", "info") #msg e categoria, info, error, ..., và anche fatto nell'html
    session.pop('user', None)
    session.pop('email', None)
    # flash("logout!", "info") #msg e categoria, info, error, ..., và anche fatto nell'html
    return redirect(url_for("login"))



if __name__ == "__main__":
    app.run(debug=True) 
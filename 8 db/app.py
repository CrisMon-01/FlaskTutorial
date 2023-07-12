from flask import Flask, redirect, url_for, render_template, request, session, flash

# db
from flask_sqlalchemy import SQLAlchemy

# gestione permanenza sessioe, fino a permanent session
from datetime import timedelta

app = Flask(__name__)
# prima di tutto secret_key è come decifro i dati della sessione (cifrati)
# per ora una cosa qualsias8i
app.secret_key="aaa"

#db
import os

# Ottenere il percorso corrente del file Python
current_path = os.path.dirname(os.path.abspath(__file__))

# Configurazione del database utilizzando il percorso corrente
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{current_path}/users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#gestione permanenza e durata sessione
app.permanent_session_lifetime = timedelta(seconds=10)

#db
db = SQLAlchemy(app)

# Model
# nelle parentesi c'è chi eredita
class users(db.Model):     
    _id = db.Column("id" ,db.Integer, primary_key= True)
    name= db.Column(db.String(100)) # se non specifico chiama come la var
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

#esempio
@app.route("/debug")
def debug():
    return "debug"

# template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all())

# template
@app.route("/login", methods=["POST","GET"])
def login():
    if request.method=="POST":
        #rendo da qui sessione permanente, default = False per non permanent
        session.permanent = True
        user = request.form['nm'] #request.form['nomecampo']
        #metto/SETTO la sessione
        session['user'] = user #<k,v>

        # lavoro nel db
        founded_users = users.query.filter_by(name=user).first() #users è il nome del modello
        if founded_users: # check esiste
            session['email'] = founded_users.email
        else: # non esiste
            usr = users(user, "") # non ho email ancora 
            db.session.add(usr) #salvo nel db
            db.session.commit() # per ogni operazione, fai commit

        flash(f"{user} logged In!", "info")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash(f"Already logged in!", "info")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user", methods=['POST','GET'])
def user():
    email = None
    #prendo sessione
    if "user" in session:
        user = session['user']

        if request.method=='POST':
            email = request.form['email']
            session['email'] = email
            #lavoro con il db
            founded_users = users.query.filter_by(name=user).first() #users è il modello
            founded_users.email=email
            db.session.commit()
            flash("Email saved")

        else:
            if "email" in session:
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
    with app.app_context():
        db.create_all()
    app.run(debug=True) 
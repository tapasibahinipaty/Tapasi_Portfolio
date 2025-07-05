# app.py  ── minimal, plain‑HTML‑form version
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)                 # ❶ no secret_key needed

# ── SQLAlchemy config ───────────────────────────────────────────
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:869190@localhost:3306/portfolio_db"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# ── database model ──────────────────────────────────────────────
class Contact(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String(50),  nullable=False)
    email      = db.Column(db.String(100), nullable=False)
    message    = db.Column(db.Text,        nullable=False)
    created_at = db.Column(db.DateTime,    default=datetime.utcnow)

with app.app_context():
    db.create_all()                   # creates table once

# ── portfolio routes ────────────────────────────────────────────
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/projects")
def projects():
    return render_template("projects.html", title="Projects")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name    = request.form["name"]
        email   = request.form["email"]
        message = request.form["message"]

        db.session.add(Contact(name=name, email=email, message=message))
        db.session.commit()

        # plain “Thank you” response; remove if you want to redirect
        return "<h2>Thank you for your message!</h2>"

    return render_template("contact.html")

# ── run app ─────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True)

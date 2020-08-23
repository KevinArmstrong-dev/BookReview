import os

from flask import Flask, session, render_template,Request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
@app.route("/home")
def index():
    return render_template("home.html")

@app.route("/register")
def register():
    return render_template("registration.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/search", methods=['GET'])
@app.route("/search/<searchTxt>", methods=['GET'])
def search(searchTxt=None):
    return render_template("search.html", searchTxt=searchTxt)

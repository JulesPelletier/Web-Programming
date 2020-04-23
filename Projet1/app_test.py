import os

from flask import Flask, session, render_template
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(engine))

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template("register.html")

@app.route('/log-in', methods=['GET', 'POST'])
def log_in():
    return render_template("login.html")

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template("home.html")


#@app.route('/<string:book_name>')
#def search_book(book_name)
#    return render_template("book.html", name=book_name)
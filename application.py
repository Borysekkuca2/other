from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import gettempdir
from Euclid import gcd, lcm

from helpers import *

# configure application
app = Flask(__name__)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# custom filter
app.jinja_env.filters["usd"] = usd

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = gettempdir()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

@app.route("/")
def index():
    return apology("TODO")
    

@app.route("/euclid", methods=["GET", "POST"])
def euclid():
    """Compute the gcd and lcm of two numbers"""
    
    #render the template "euclid"
    if request.method == "GET":
        return render_template("euclid.html")
    
    if request.method == "POST":
        
        #if the first number is not provided, return apology
        if not request.form.get("first"):
            return apology("must provide a number")
        
        first = int(request.form.get("first"))
        
        #if the second number not provided, return apology
        if not request.form.get("second"):
            return apology("must provide a number")
        
        second = int(request.form.get("second"))

        
        #if numbers less than 0, return apology
        if first <= 0:
            return apology("must provide a positive integer")
            
        if second <= 0:
            return apology("must provide a positive integer")
        
        divisor = gcd(first, second)
        multiplicity = lcm(first, second)
        
        # redirect user to index
        return render_template("gcd_lcm.html", x = first, y = second, gcd = divisor, lcm = multiplicity)
        
@app.route("/polynomials", methods=["GET", "POST"])
def polynomials():
    """Compute the gcd and lcm of two numbers"""
    
    #render the template "polynomial"
    if request.method == "GET":
        return render_template("polynomials.html")
    
    if request.method == "POST":
        
        #if the first number is not provided, return apology
        if not request.form.get("first"):
            return apology("must provide the degree of the dividend")
        
        first = int(request.form.get("first"))
        
        #if the second number not provided, return apology
        if not request.form.get("second"):
            return apology("must provide the degree of the divisor")
        
        second = int(request.form.get("second"))

        
        #if numbers less than 0, return apology
        if first <= 0:
            return apology("must provide positive integers")
            
        if second <= 0:
            return apology("must provide positive integers")
        
        if second > first:
            return apology("the degree of the divisor cannot be greater than the degree of the divisor")
        
        # redirect user to index
        return apology("not done yet")

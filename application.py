from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import gettempdir
from Euclid import gcd, lcm
from polynomials1 import polynomial

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

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = gettempdir()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/start")
def index():
    return render_template("start.html")
    

@app.route("/euclid", methods=["GET", "POST"])
def euclid():
    """Compute the gcd and lcm of two numbers"""
    
    # render the template "euclid"
    if request.method == "GET":
        return render_template("euclid.html")
    
    if request.method == "POST":
        
        # if the first number is not provided, return apology
        if not request.form.get("first"):
            return apology("must provide a number")
        
        # if the second number not provided, return apology
        if not request.form.get("second"):
            return apology("must provide a number")

        # extract the numbers from the request form
        first = int(request.form.get("first"))        
        second = int(request.form.get("second"))

        # if numbers less than 0, return apology
        if first <= 0:
            return apology("must provide a positive integer")
            
        if second <= 0:
            return apology("must provide a positive integer")
        
        # calculate gcd and lcm
        divisor = gcd(first, second)
        multiplicity = lcm(first, second)
        
        # render a template that will show the results
        return render_template("gcd_lcm.html", x = first, y = second, gcd = divisor, lcm = multiplicity)
        
@app.route("/polynomials", methods=["GET", "POST"])
def polynomials():
    """Type the degrees of the dividend and the divisor"""
    
    # render the template "polynomial"
    if request.method == "GET":
        return render_template("polynomials.html")
    
    if request.method == "POST":
        
        # if the first number is not provided, return apology
        if not request.form.get("first"):
            return apology("must provide the degree of the dividend")
        
        # extract the degree of the dividend from the request form
        first = int(request.form.get("first"))
        
        # if the second number not provided, return apology
        if not request.form.get("second"):
            return apology("must provide the degree of the divisor")
                
        # extract the degree of the divisor from the request form
        second = int(request.form.get("second"))
        
        # if degrees less than 0, return apology
        if first <= 0:
            return apology("must provide positive integers")
            
        if second <= 0:
            return apology("must provide positive integers")
        
        # if the degree of divisor is greater than the degree of the dividend, return apology
        if second > first:
            return apology("the degree of the divisor cannot be greater than the degree of the divisor")
        
        # store the degrees of both polynomials as session variables
        session["first"] = first
        session["second"] = second
        
        # redirect user to the page where they can input the coefficients of the polynomials
        return redirect(url_for("coefficients"))

@app.route("/coefficients", methods=["GET", "POST"])
def coefficients():
    """ Type the coefficients of the dividend and divisor """
    
    # extract the degrees of both polynomials
    first = session["first"]
    second = session["second"]    
    
    # render the template "coefficients"
    if request.method == "GET":

        return render_template("coefficients.html", first = first, second = second)

    if request.method == "POST":
        
        # declare the list of coefficients of the dividend and divisor
        dividend = []
        divisor = []
        
        # iterate over the coefficients of the dividend
        for i in range(first+1):
            
            # access the coefficient from the website
            coefficient = request.form.get(str(i))

            # if no coefficient provided, return apology
            if not coefficient:
                return apology("must provide a coefficient")
            
            # else append the coefficient to the list of dividend coefficients
            else:
                dividend.append(float(coefficient))

        # iterate over the coefficients of the divisor
        for i in range(second+1):
            
            # access the coefficient from the website
            coefficient = request.form.get("b" + str(i))

            # if no coefficient provided, return apology
            if not coefficient:
                return apology("must provide a coefficient")
            
            # else append the coefficient to the list of divisor coefficients
            else:
                divisor.append(float(coefficient))
        
        # store the coefficients of the dividend and divisor as session variables
        session["dividend"] = dividend
        session["divisor"] = divisor

        # redirect the user to the page where they can see the result of the division
        return redirect(url_for("division"))

@app.route("/division", methods=["GET"])
def division():
    """ Shows the result of the division """
    
    # extract the coefficients of the dividend and divisor
    dividend = session["dividend"]
    divisor = session["divisor"]
    
    # perform the division
    result = polynomial(dividend, divisor)  
    
    # the function "polynomial" returns the list of two elements
    # the first element in this list is the list of quotient coefficients, and the second one is the list of remainder coefficients
    quotient = result[0]
    remainder = result[1]
    
    # render a template with results
    return render_template("division.html", len1 = len(dividend), len2 = len(divisor), len3 = len(quotient), len4 = len(remainder), dividend = dividend, divisor = divisor, quotient = quotient, remainder = remainder)


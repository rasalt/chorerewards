from flask import render_template

from flask import request, redirect, url_for
from flask import flash
from flask.ext.login import login_user, login_required, current_user, logout_user


from chorerewards import app
from .models import User
from .database import session

@app.route("/login", methods=["GET"])
def login_get():
    return render_template("login.html")

@app.route("/register1", methods=["GET"])
def register1_get():
  return render_template("register1.html")

@app.route("/register1", methods=["POST"])
def register1_post():
  print "register1_post"
  
  # Check if passwords match spit error if it does
  pass1 = request.form["password1"]
  pass2 = request.form["password2"]
  if (pass1 != pass2) or not (pass1 and pass2):
    flash("Password either doesn't match or empty, please check")
    return redirect(url_for("register1_get"))


  # Create user
  
  # Check if email exists in the database spit error if it does
  email = request.form["emailaddr"]
  if session.query(User).filter_by(emailaddr=email).first():
    print "User with that email address already exists"
    flash("Incorrect username, email already registered", "danger")
    return redirect(url_for("register1_get"))

  # All good go ahead and register
  user = User(name = request.form["name"], familyname = request.form["familyname"], 
                  emailaddr = request.form["emailaddr"], passwd = request.form["password1"],
                  role = "admin")
                  
  session.add(user)
  session.commit()
  return redirect(url_for("login_get"))

@app.route("/register2", methods=["GET"])
def register2_get():
  return render_template("register2.html")

#@app.route("/register2", methods=["POST"])

#def register2_post():
#  if request.form["button"] == "add":
#    User = User(name = request.form["emailaddr"])
#    Users.append(User)
#    return render_template("register21.html", Users=Users)
#  else:
#    if request.form["emailaddr"] != "":
#      User = User(name = request.form["emailaddr"])
#      Users.append(User)
#      return render_template("register_done.html")
    
  
  


    
@app.route("/")
def dashboard():
  print "In route"
  return render_template("dashboard.html")
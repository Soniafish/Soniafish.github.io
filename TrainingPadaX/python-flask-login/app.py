# !/usr/bin/python2
# coding:utf-8

from flask import Flask     
from flask import request
from flask import redirect
from flask import render_template   
from flask import session

app=Flask(__name__)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route("/")
def index():
    if 'username' in session:
        return redirect("/member")
    else:
        return render_template("default.html")


@app.route("/signin", methods=["POST", "GET"])
def handel_signin():
    if request.method == 'POST':
        account=request.form["account"]
        password=request.form["pword"]
        
        if account=="test" and password=="test":
            session['username'] = account
            return redirect("/member")
        else:
            return redirect("/error")

    else:
        if 'username' in session:
            return redirect("/member")
        else:
            return redirect("/default")
    
@app.route("/member")
def check_member():
    # if session["username"]=="test":
    if 'username' in session:
        return render_template("member.html")
    else:
        return redirect("/")
    
@app.route("/error")
def show_error():
    return render_template("error.html")

@app.route('/signout')
def signout():
    # session.pop('username', "")
    session.pop('username', None)
    return render_template("default.html")


print("Logged in as %s") 
app.run(port=3000)
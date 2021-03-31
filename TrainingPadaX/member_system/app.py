# !/usr/bin/python2
# coding:utf-8

from flask import Flask     
from flask import request
from flask import redirect
from flask import render_template   
from flask import session
import pandas as pd
import pymysql

db_settings = {
    "host": "127.0.0.1",    #主機
    "port": 3306,           #埠號    
    "user": "root",         #使用者名稱
    "password": "12980541", #使用者帳號
    "db": "website",        #資料庫名稱
}

app=Flask(__name__)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route("/")
def index():
    if 'userid' in session:
        return redirect("/member")
    else:
        return render_template("default.html")


@app.route("/signin", methods=["POST", "GET"]) #登入
def handel_signin():
    if request.method == 'POST':
        userid=request.form["userid"]
        userpw=request.form["userpw"]
        
        # 連線DB
        cnnt=db_connect()
        
        # 建立Cursor物件
        cursor=cnnt.cursor()

        # 取得所有資料
        cursor.execute("SELECT * FROM user")
        db_user=cursor.fetchall()

        # 確認登入是否正確
        for row in db_user:
            if row[2]==userid and row[3]==userpw:
                # erro_message=""
                session['userid'] = userid
                session['username'] = row[1]
                return redirect("/member?name="+row[1]) 

        return redirect("/error?message=帳號或密碼輸入錯誤")

    else:
        if 'userid' in session:
            return redirect("/member")
        else:
            return redirect("/")

@app.route("/signup", methods=["POST", "GET"])  #註冊
def handel_signup():
    if request.method == 'POST':
        username=request.form["username"]
        userid=request.form["userid"]
        userpw=request.form["userpw"]
        
        # 連線DB
        cnnt=db_connect()
        
        # 建立Cursor物件
        cursor=cnnt.cursor()

        # 取得所有資料
        cursor.execute("SELECT * FROM user")
        db_user=cursor.fetchall()
        # print(db_user)
        for row in db_user:
            if row[2]==userid:  # 註冊失敗
                return redirect("/error?message=帳號已經被註冊")

        # 註冊成功
        cursor.execute("INSERT INTO user(name, username, password)VALUES('" + username + "','" + userid + "', '" + userpw + "')")
        cnnt.commit()

        return redirect("/") 

    else:
        if 'userid' in session:
            return redirect("/member")
        else:
            return redirect("/")
    
@app.route("/member")
def check_member():
    if 'userid' in session:
        name = request.args.get("name", None)
        return render_template("member.html", name=name)
    else:
        return redirect("/")
    
@app.route("/error")
def show_error():
    message = request.args.get("message", None)
    return render_template("error.html", message=message)

@app.route('/signout')
def signout():
    session.pop('username', None)
    session.pop('userid', None)
    return redirect("/")

#連線DB
def db_connect():
    try:
        # 建立Connection物件
        connect = pymysql.connect(**db_settings)
        print("connect db_settings")

        # 建立Cursor物件
        # db_cursor=connect.cursor()

        return connect

    except Exception as ex:
        print(ex)
        return "資料庫連線失敗"


app.run(port=3000)
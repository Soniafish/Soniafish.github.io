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

def db_connect():
    try:
        # 建立Connection物件
        connect = pymysql.connect(**db_settings)
        print("connect db_settings")

        return connect

    except Exception as ex:
        print(ex)
        return "資料庫連線失敗"

# 連線DB
cnnt=db_connect()

# 建立Cursor物件
cursor=cnnt.cursor()


app=Flask(__name__)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route("/")
def index():
    if 'userid' in session:
        return redirect("/member?name="+session['username'])
    else:
        return render_template("default.html")


@app.route("/signin", methods=["POST", "GET"]) #登入
def handel_signin():
    if request.method == 'POST':
        userid=request.form["userid"]
        userpw=request.form["userpw"]

        # 篩選資料表的資料
        result=cursor.execute("SELECT name FROM user where username='"+userid+"' and password='"+userpw+"'")
        print(result)
        if result:   # 登入成功：即帳號/密碼皆存在資料表
            select_data=cursor.fetchone()   #取得使用者名字
            session['userid'] = userid
            session['username'] = select_data[0]
            return redirect("/member?name="+select_data[0]) 
        
        # 登入失敗：即帳號或密碼不存在資料表
        return redirect("/error?message=帳號或密碼輸入錯誤")

    else:
        if 'userid' in session:
            return redirect("/member?name="+session['username'])
        else:
            return redirect("/")

@app.route("/signup", methods=["POST", "GET"])  #註冊
def handel_signup():
    if request.method == 'POST':
        username=request.form["username"]
        userid=request.form["userid"]
        userpw=request.form["userpw"]

        # 篩選資料表的資料
        result=cursor.execute("SELECT * FROM user where username='"+userid+"'")
        print(result)
        if result: # 註冊失敗:即資料表已有該使用者帳號
            return redirect("/error?message=帳號已經被註冊")
        
        
        # 註冊成功：即資料表無該使用者帳號
        cursor.execute("INSERT INTO user(name, username, password)VALUES('" + username + "','" + userid + "', '" + userpw + "')")
        cnnt.commit()

        return redirect("/") 

    else:
        if 'userid' in session:
            return redirect("/member?name="+session['username'])
        else:
            return redirect("/")
    
@app.route("/member")
def check_member():
    if 'userid' in session:
        name = request.args.get("name", session['username'])
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




app.run(port=3000)
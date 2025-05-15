from flask import Flask,render_template,request
import mysql.connecter
import re
app = Flask(__name__)
@app.route('/login',methods=["GET","POST"])
def login():
    msg = ''
    if request.method == "POST" and "username" in requset.form and 'password' in request.form:
        username = 
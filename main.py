from flask import Flask, request, redirect, render_template
import os
import re
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

usr_error = ""
pass_1_error = ""
pass_2_error = ""
email_error = ""

@app.route("/validate", methods=["POST"])
def validate():
    #initial simple validation, confirm base requirments...
    #check user name and password fields  then check e-mail
    usr_name = request.form['user_name']
    password1 = request.form['pass']
    password2 = request.form['pass_c']
    email = request.form['e_mail']

    if (not usr_name or usr_name.strip() ==""):
        error = "Please enter a user name."
        usr_name = ""
        return redirect("/signup/?error=" + error)
    
    if (len(usr_name) < 3 or len(usr_name) > 20):
        error = "Usernames must be longer than 3 characters"
        usr_name = ""
        return redirect("/signup/?error=" + error)

    if space(usr_name) == False:
        error ="Usernames may not contain spaces"
        usr_name = ""
        return redirect("/signup/?error=" + error)

    if (not password1 ==password2):
        password1 =""   




        



   
    return render_template('welcome.html', usr_name)

def space(text):
    sp = " "
    if sp not in text:
        return True
    else:
        return False    

def mail(text):

    return True


@app.route("/signup", methods=["GET", "POST"])
def index():
    encoded_error = request.args.get("error")
    return render_template('signup.html', )


app.run()
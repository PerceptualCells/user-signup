from flask import Flask, request, redirect, render_template
import os
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
    #error messages
    usr_error = ""
    pass_1_error = ""
    pass_2_error = ""
    email_error = ""
    error = ""
    # Validate Username
    if not has_val(usr_name):
        usr_error = "You have left a necessary field blank :}"
        
    if not length(usr_name):
        usr_error = "Your username is too long or too short"

    if  not usr_name.isalnum():
        usr_error = "You have invalid characters in your username"

    if not space(usr_name):
        usr_error = "you have spaces in your username"

    # Validate Password
    if usr_name == password1:
        usr_error = "your username and password may not be the same"
        p_error= "your username and password may not be the same"
     
    if not has_val(password1) or not has_val(password2):
        p_error ="You have left a necessary field blank"

    if password1 != password2:
        p_error = "Your passwords must match"
        p2_error = "Your passwords must match"

    if not space(password1):
        p_error = "passwords cannot have spaces"

    
    if not length(password1):
        p_error = "password length outside of range (3 < password < 20)"
        
    if not password1.isalnum():
        p_error = "you have unaccepable symbols in your password"

    # validate username
    #if has_val(usr_name):
    #    if e-mail(usr_name):

        
    """
    if not usr_error and not pass_1_error and not pass_2_error and not email_error:
        return render_template("welcome.html", usr_name = usr_name)
    else:
        return render_template ("signup.html",
        user_name = usr_name,
        e_mail = email,
        password = "",
        usr_error = usr_error)
    """

    
    #TEST RETURN
    if error=="":
        return render_template("welcome.html",
         user_name = usr_name)
    else:
        return render_template("signup.html",
     usr_error = usr_error, p_error = p_error, user_name = usr_name)    

def has_val(text):
    if text == "" or text.strip() == "":
        return False
    else:
        return True    

def space(text):
    sp = " "
    if sp not in text:
        return True
    else:
        return False

def length(text):
    if len(text) >= 3 or len(text) <= 20:
        return True
    else:
        return False

#def e-mail(text):
    if space(text):




 


@app.route("/signup", methods=["GET", "POST"])
def index():
    return render_template('signup.html')


app.run()
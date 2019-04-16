from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

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
    p_error = ""
    p2_error = ""
    email_error = ""
    
    # Validate Username
    if usr_name == password1:
        usr_error = "your username and password may not be the same"
        p_error= "your username and password may not be the same"

    
        
    if not length(usr_name):
        usr_error = "Your username is too long or too short"

    if  not usr_name.isalnum():
        usr_error = "You have invalid characters in your username"

    if not space(usr_name):
        usr_error = "you have spaces in your username"

    if not has_val(usr_name):
        usr_error = "The username field cannot be blank :}"
    # Validate Password
    

    if password1 != password2:
        p_error = "Your passwords must match"
        p2_error = "Your passwords must match"

    if not space(password1):
        p_error = "passwords cannot have spaces"
   
    if not length(password1):
        p_error = "password length outside of range (3 < password < 20)"
    

    if not password1.isalnum():
        p_error = "you have unaccepable symbols in your password"

    if not has_val(password1) or not has_val(password2):
        p_error ="You have left a necessary field blank"    

    # validate username
    if has_val(email):
        if not email_chk(email):
            email_error = "this is not a valid email address"
    else:
        email_error = ""    


    #TEST RETURN
    if usr_error=="" and p_error == "" and p2_error == "" and email_error == "":
        return render_template("welcome.html",
            user_name = usr_name)
    else:
        return render_template("signup.html", usr_error = usr_error,
            p_error = p_error,
            user_name = usr_name,
            e_error = email_error,
            p2_error = p2_error)    

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
    if len(text) >= 3 and len(text) <= 20:
        return True
    else:
        return False

def email_chk(text):
    if space(text) and length(text):
        if "@" in text and "." in text:
            return True
    else:
        return False    

@app.route("/signup", methods=["GET", "POST"])
def index():
    return render_template("signup.html")


app.run()
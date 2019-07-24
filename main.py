from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
    
    return render_template('index.html',title="User Sign up")



@app.route("/", methods=['POST'])
def validate():

    username = request.form['username']
    password = request.form['password']
    password2 = request.form['password2']
    email = request.form['email']
    error = ""
#username validation
     #username is empty
    if username == "":
        error = "You cannot have an empty username"
        return render_template('index.html',username_error=error,username=username,email=email)

    #username is not the right length
    if len(username) < 3 or len(username) > 20:
        error = "Your username has to be atleast 3 characters long but no more than 20"
        return render_template('index.html',title="Signup Error",username_error=error,username=username,email=email)

    #username has a space
    if " " in username:
        error = "You cannot have a space in your username"
        return render_template('index.html',title="Signup Error",username_error=error,username=username,email=email)

#password validation
    #password is empty
    if password == "":
        error = "You cannot have an empty password"
        return render_template('index.html',title="Signup Error",password_error=error,username=username,email=email)

    #password is not the right length
    if len(password) < 3 or len(password) > 20:
        error = "Your password has to be atleast 3 characters long but no more than 20"
        return render_template('index.html',title="Signup Error",password_error=error,username=username,email=email)

    #password has a space
    if " " in password:
        error = "You cannot have a space in your username"
        return render_template('index.html',title="Signup Error",password_error=error,username=username,email=email)

    #passwords do not match
    if password != password2:
        error = "Your passwords do not match"
        return render_template('index.html',title="Signup Error",password_error=error,username=username,email=email)

#email validation
    #email does not have an @
    if "@" not in email:
        error = "You do not have a valid email"
        return render_template('index.html',title="Signup Error",email_error=error,username=username,email=email)

    if "." not in email:
        error = "You do not have a valid email"
        return render_template('index.html',title="Signup Error",email_error=error,username=username,email=email)

        
    
    return redirect("/Welcome?username=" + username)
    
@app.route("/Welcome", methods=['GET'])
def welcome():
    username = request.args.get("username")
    return render_template('welcome.html',title="Welcome",username=username)

app.run()
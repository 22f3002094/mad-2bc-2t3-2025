from flask import current_app as app
from flask import request
from .models import User
from flask_security import verify_password , auth_required, roles_required
@app.route("/")
def index():
    return "hello world"


@app.route("/login" , methods = ["GET" ,"POST"])
def login():
    if request.method=="POST":
        email = request.json.get("email")
        password = request.json.get("password")
        user = User.query.filter_by(email=email).first()
        if not email or not password:
            return "Email and Password required" , 400
        elif user is None:
            return "User not found" , 404
        elif  verify_password(password , user.password)  == False:
            return "Invalid password" , 401
        else:
            token = user.get_auth_token()
            print("Generated Token :" , token)
            return {"name" :user.name , "token" : token , "message" :"Login Successful"} , 200
    else :
        return "hello world"
    
@app.route("/protected")
@auth_required("token")
@roles_required("Student")
def protected():
    return "You have accessed a protected route"
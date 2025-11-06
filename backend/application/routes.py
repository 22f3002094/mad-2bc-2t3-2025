from flask import current_app as app
from flask import request , render_template
from .models import User
from flask_security import verify_password , auth_required, roles_required
from flask_security import hash_password

from .models import *
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login" , methods = ["GET" ,"POST"])
def login():
    if request.method=="POST":
        email = request.json.get("email")
        password = request.json.get("password")
        user = User.query.filter_by(email=email).first()
        if not email or not password:
            return {"message" :"Email and Password required" }, 400
        elif user is None:
            return {"message" :"User not found" }  , 404
        elif  verify_password(password , user.password)  == False:
            return {"message":"Invalid password" }, 401
        else:
            token = user.get_auth_token()
            print("Generated Token :" , token)
            return {"name" :user.name , "token" : token , "message" : "Login Successful!!"} , 200
    else :
        return "hello world"
    
@app.route("/protected")
@auth_required("token")
@roles_required("Student")
def protected():
    return "You have accessed a protected route"


@app.route("/register" ,methods=["POST"])
def register():
    if request.method=="POST":
        name = request.json.get("name")
        email = request.json.get("email")
        password = request.json.get("password")
        if not name or not email or not password:
            return   {"message" :"Name , Email and Password required"} , 400
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return  {"message" : "User with this email already exists"} , 409
        else:
            datastore = app.security.datastore
            datastore.create_user( name = name , email=email , password = hash_password(password),roles = ["Student"])
            
            db.session.commit()
            return {"message" : "User registered successfully"} , 201
        
@app.route("/subject" , methods = ["GET" , "POST" , "PUT" , "DELETE"])
# @auth_required("token")
def subject():
    if request.method =="GET" : 
        if request.args.get("query_type") =="all":
            subjects = Subject.query.all()
            subs=[]
            for sub in subjects:
                subs.append({"name" : sub.name , "description" : sub.description , "id" :sub.id})
            return subs
        elif request.args.get("sub_id") :
            id = request.args.get("sub_id")
            subject = Subject.query.filter_by(id = id ).first()
            if subject:
                sub = {"name" : subject.name , "description" : subject.description , "id" :subject.id}
                return sub,200
            else:
                return {"message" : "Subject not found"} , 404
            
        elif request.args.get("sub_name"):
            n = request.args.get("sub_name")
            subjects = Subject.query.filter(Subject.name.ilike(f"%{n}%")).all()
            subs=[]
            for sub in subjects:
                subs.append({"name" : sub.name , "description" : sub.description , "id" :sub.id})
            return subs


    elif request.method=="POST":
        sub_name = request.json.get("name")
        sub_desc = request.json.get("description")

        subject = Subject.query.filter(Subject.name.ilike(f"%{sub_name}%")).first()
        if subject:
            return {"message" : "Subject already exist" } , 409
        
        else: 
            subject = Subject(name = sub_name.capitalize(), description = sub_desc)
            db.session.add(subject)
            db.session.commit()
            return {"name": subject.name , "description" : subject.description , "id" : subject.id } , 201
    elif request.method =="PUT":
        id = request.json.get("sub_id")
        sub_name = request.json.get("name")
        sub_desc = request.json.get("description")

        subject = Subject.query.filter_by(id = id ).first()
        if subject:
            if sub_name:
                same_subname = Subject.query.filter(Subject.name.ilike(f"%{sub_name}%")).first()
                if same_subname and same_subname.id != subject.id:
                    return {"message" : "Subject with this name already exist"} , 409
                subject.name = sub_name.capitalize()
            if sub_desc:
                subject.description = sub_desc
            db.session.commit()
            return {"name": subject.name , "description" : subject.description , "id" : subject.id } , 200
        else:
            return {"message" : "Subject not found"} , 404
        
    elif request.method =="DELETE":
        id = request.args.get("sub_id")
        subject = Subject.query.filter_by(id = id ).first()
        if subject:
            db.session.delete(subject)
            db.session.commit()
            return {"message" : "Subject deleted successfully"} , 200
        else:
            return {"message" : "Subject not found"} , 404
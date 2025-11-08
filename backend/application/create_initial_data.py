from flask import current_app as app
from .models import *
from flask_security import hash_password 
from datetime import datetime 

with app.app_context():
    db.create_all()
    datastore = app.security.datastore
    datastore.find_or_create_role(name="Admin")
    datastore.find_or_create_role(name="Student")
    if not datastore.find_user(email = "h@gmail.com"):
        datastore.create_user(name = "Himanshu" , email="h@gmail.com" , password = hash_password("pass"),roles = ["Admin"])
    if not datastore.find_user(email = "stud1@gmail.com"):
        datastore.create_user(name = "stud1" , email="stud1@gmail.com" , password = hash_password("pass"),roles = ["Student"])
    db.session.commit()

    if Subject.query.count() ==0 :
        subjects = [
            Subject(name="Python" , description = "xyz") , 
            Subject(name = "Math" , description = "dfsdg")
        ]
        db.session.add_all(subjects)
        db.session.commit()
    if Quiz.query.count() == 0:
        quizs = [ 
            Quiz(title = "String Operations" ,total_marks = 50 , date = datetime(2025, 11, 10) , duration = 60 , description="this is string operations quiz" , sub_id = 1) ,
            Quiz(title = "File Handling" ,total_marks = 50 , date = datetime(2025, 11, 10) , duration = 60 , description="this is file handling quiz" , sub_id = 1) 
        ]
        db.session.add_all(quizs)
        db.session.commit()
    print("initial data is created")



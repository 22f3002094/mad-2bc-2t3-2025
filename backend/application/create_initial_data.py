from flask import current_app as app
from .models import *
from flask_security import hash_password 

with app.app_context():
    db.create_all()
    datastore = app.security.datastore
    datastore.find_or_create_role(name="Admin")
    datastore.find_or_create_role(name="Student")
    if not datastore.find_user(email = "h@gmail.com"):
        datastore.create_user(name = "Himanshu" , email="h@gmail.com" , password = hash_password("pass"),roles = ["Admin"])
    db.session.commit()

    if Subject.query.count() ==0 :
        subjects = [
            Subject(name="Python" , description = "xyz") , 
            Subject(name = "Math" , description = "dfsdg")
        ]
        db.session.add_all(subjects)
        db.session.commit()
    print("initial data is created")



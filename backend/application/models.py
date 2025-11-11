from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin , RoleMixin
db = SQLAlchemy()


class User(db.Model , UserMixin):
    __tablename__  ="user"
    id = db.Column(db.Integer , primary_key= True)
    name= db.Column(db.String , nullable = False)
    email = db.Column(db.String ,nullable = False , unique = True)
    password = db.Column(db.String , nullable = False)
    active = db.Column(db.Boolean , nullable  = False , default = True)
    fs_uniquifier = db.Column(db.String , nullable = False , unique = True)
    roles = db.relationship("Role" , backref = "users" ,secondary = "user_roles" )
    scores = db.relationship("Scores" , backref = "user" )

class Role(db.Model ,RoleMixin):
    __tablename__  ="role"
    id = db.Column(db.Integer , primary_key= True)
    name = db.Column(db.String )

class User_Roles(db.Model):
    __tablename__  ="user_roles"
    id =  db.Column(db.Integer , primary_key= True)
    user_id = db.Column(db.Integer , db.ForeignKey("user.id") , nullable = False)
    role_id = db.Column(db.Integer , db.ForeignKey("role.id") , nullable = False)

class Subject(db.Model):
    __tablename__  ="subject"
    id = db.Column(db.Integer , primary_key= True)
    name = db.Column(db.String , nullable = False , unique = True)
    description = db.Column(db.String )
    quizes = db.relationship("Quiz" , backref = "subject" )



class Quiz(db.Model):
    __tablename__  ="quiz"
    id = db.Column(db.Integer , primary_key= True)
    title = db.Column(db.String , nullable = False)
    description = db.Column(db.String )
    sub_id = db.Column(db.Integer , db.ForeignKey("subject.id") , nullable = False)
    total_marks = db.Column(db.Integer , nullable = False)
    date  = db.Column(db.DateTime)
    duration = db.Column(db.Integer ) 
    questions = db.relationship("Question" , backref = "quiz" )
    scores = db.relationship("Scores" , backref = "quiz" )

class Question(db.Model):
    __tablename__  ="question"
    id = db.Column(db.Integer , primary_key= True)
    quiz_id = db.Column(db.Integer , db.ForeignKey("quiz.id") , nullable = False)
    statement = db.Column(db.String , nullable = False)
    option_a = db.Column(db.String , nullable = False)
    option_b = db.Column(db.String , nullable = False)
    option_c = db.Column(db.String , nullable = False)
    option_d = db.Column(db.String , nullable = False)
    correct_option = db.Column(db.String , nullable = False)
    marks = db.Column(db.Integer , nullable = False)

class Scores(db.Model):
    __tablename__  ="scores"
    id = db.Column(db.Integer , primary_key= True)
    user_id = db.Column(db.Integer , db.ForeignKey("user.id") , nullable = False)
    quiz_id = db.Column(db.Integer , db.ForeignKey("quiz.id") , nullable = False)
    score = db.Column(db.Integer , nullable = False)
    date_attempted = db.Column(db.DateTime)
    attempt  = db.Column(db.JSON , nullable = True)



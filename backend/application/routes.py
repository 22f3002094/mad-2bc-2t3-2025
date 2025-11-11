from flask import current_app as app
from flask import request , render_template
from .models import User
from flask_security import verify_password , auth_required, roles_required
from flask_security import hash_password , current_user
from datetime import datetime

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

            return {"name" :user.name , "token" : token ,"role" :user.roles[0].name , "message" : "Login Successful!!"} , 200
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
@auth_required("token")
def subject():
    if request.method =="GET" : 
        if request.args.get("query_type") =="all":
            subjects = Subject.query.all()
            subs=[]
            for sub in subjects:
                subs.append({"name" : sub.name , "description" : sub.description , "id" :sub.id})
            return subs,200
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
        id = request.json.get("id")
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
        

@app.route("/student" , methods=["GET" , "POST" ])
@auth_required("token")
def students():
    if request.method =="GET":
        if request.args.get("query_type") =="all":
            role = Role.query.filter_by(name ="Student").first()
            students=[]
            for user in role.users: 
                students.append({"id" : user.id , "name": user.name , "email":user.email, "status":"Active" if user.active else "Flagged" })

            return students  , 200
        
@app.route("/quiz" , methods=["GET","POST" , "PUT" , "DELETE"] )
@auth_required("token")
def quiz():
    if request.method=="GET":
        if request.args.get("subname") :
            subname = request.args.get("subname")
            subobj = Subject.query.filter_by(name=subname ).first()
            if not subobj:
                return {"message":"Subject not found"} , 404
            quizes = []
            for quiz in subobj.quizes:
                quizes.append({"id":quiz.id ,"date" : datetime.strftime(quiz.date , "%Y-%m-%d"), "title" : quiz.title , "no_of_questions": len(quiz.questions) , "total_marks" : quiz.total_marks} )   
            return quizes, 200
        if request.args.get("quiz_id"):
            id = request.args.get("quiz_id")
            quiz = Quiz.query.filter_by(id = id).first()
            if not quiz:
                return {"message" : "Quiz not found"} , 404
            quiz_data = {"title" : quiz.title, "id" : quiz.id , "description" : quiz.description,
                         "total_marks" :quiz.total_marks, "date" :datetime.strftime(quiz.date , "%Y-%m-%d"), "duration" : quiz.duration,
                         } 
            quiz_data["questions"] = []
            for question in quiz.questions:
                quiz_data["questions"].append({"id": question.id , "statement" : question.statement,
                                              "option_a" :question.option_a ,
                                                "option_b" : question.option_b , "option_c" : question.option_c ,
                                                "option_d": question.option_d , "correct_option" : question.correct_option ,
                                                "marks" : question.marks})
            print(quiz_data)
            return quiz_data,200

            

    if request.method== "POST":
        print("hello")
        subname = request.args.get("sub_name")
        subobj = Subject.query.filter_by(name=subname ).first()
        
        if not subobj:
            return {"message":"Subject not found"} , 404
        data = request.get_json()
        data["date"] = datetime.strptime(data["date"] , "%Y-%m-%d")
        newquiz  = Quiz(title = data["title"] ,total_marks=0, description = data["description"] , date = data["date"] , duration = data["duration"] , sub_id= subobj.id )
        db.session.add(newquiz)
        db.session.commit()
        total_marks = 0
        for question in data["questions"]:
            new_ques = Question(statement = question["statement"] , option_a = question["option_a"] ,
                                option_b  = question["option_b"] , option_c = question["option_c"] ,
                                option_d = question["option_d"] , correct_option = question["correct_option"] ,
                                marks = question["marks"] , quiz_id= newquiz.id )
            total_marks+=int(question["marks"])
            db.session.add(new_ques)
            db.session.commit()
        newquiz.total_marks = total_marks
        db.session.commit()
        return {"message" : "Quiz Create Succesfully" } , 201
    if request.method=="PUT":
        data =request.get_json()
        id = request.args.get("quiz_id")
        quizobj = Quiz.query.filter_by(id = id).first()
        if data["title"]:
            quizobj.title = data["title"]
        if data["description"]:
            quizobj.description = data["description"]
        if data["date"]:
            data["date"] = datetime.strptime(data["date"] , "%Y-%m-%d")
            quizobj.date = data["date"]
        if data["duration"]:
            quizobj.duration = data["duration"]
        total_marks = 0
        for existing_question in quizobj.questions:
            for question in data["questions"]:
                if question.get("id") and question.get("id") == existing_question.id:
                    if question["statement"]:
                        existing_question.statement = question["statement"]
                    if question["option_a"]:
                        existing_question.option_a  = question["option_a"]
                    if question["option_b"]:
                        existing_question.option_b  = question["option_b"]
                    if question["option_c"]:
                        existing_question.option_c  = question["option_c"]
                    if question["option_d"]:
                        existing_question.option_d  = question["option_d"]
                    if question["correct_option"]:
                        existing_question.correct_option  = question["correct_option"]
                    if question["marks"]:
                        existing_question.marks  = question["marks"]
                        total_marks += int(question["marks"])
                    db.session.commit()
                elif not question.get("id"):
                    new_ques = Question(statement = question["statement"] , option_a = question["option_a"] ,
                                option_b  = question["option_b"] , option_c = question["option_c"] ,
                                option_d = question["option_d"] , correct_option = question["correct_option"] ,
                                marks = question["marks"] , quiz_id= quizobj.id )
                    db.session.add(new_ques)
                    db.session.commit()
                    total_marks += int(question["marks"])
                
        quizobj.total_marks = total_marks
        db.session.commit()
        return "xyz" , 200



@app.route("/quiz/attempt" , methods=["POST" , "GET"]) 
@auth_required("token")
def attempt_quiz():
    if request.method=="GET":
        if request.args.get("quiz_id"):
            id = request.args.get("quiz_id")
            quiz = db.session.query(Quiz).filter_by(id = id).first()
            if not quiz:
                return {"message" : "Quiz not found"} , 404
            if quiz.date and quiz.date.date() ==datetime.now().date():
                score = Scores.query.filter_by(user_id = current_user.id , quiz_id = quiz.id).first()
                if score:
                    return {"message" : "You have already attempted this quiz"} , 403
                quiz_data = {"title" : quiz.title, "id" : quiz.id , "description" : quiz.description,
                         "total_marks" :quiz.total_marks, "date" :datetime.strftime(quiz.date , "%Y-%m-%d"), "duration" : quiz.duration,
                         } 
                quiz_data["questions"] = []
                for question in quiz.questions:
                    quiz_data["questions"].append({"id": question.id , "statement" : question.statement,
                                                "option_a" :question.option_a ,
                                                    "option_b" : question.option_b , "option_c" : question.option_c ,
                                                    "option_d": question.option_d , "correct_option" : question.correct_option ,
                                                    "marks" : question.marks})

                return quiz_data , 200
            elif quiz.date and quiz.date.date() <=datetime.now().date():
                return {"message" : "Due date passed, Can't attempt the quiz"} , 403 
            elif quiz.date and quiz.date.date() >=datetime.now().date():
                return {"message" : f"Can't Attempt the Quiz early. Come back on {quiz.date.date()}"} , 403 
    if request.method=="POST":
        attempt_data = request.get_json()
        quiz_id = attempt_data["quiz_id"]
        options_selected = attempt_data["options_selected"]
        print(options_selected)
        quiz =Quiz.query.filter_by(id = quiz_id).first()
        if not quiz:
            return {"message" : "Quiz not found"} , 404
        total_score = 0
        for i in range(len(quiz.questions)):
            if quiz.questions[i].correct_option == options_selected[i]:
                total_score += quiz.questions[i].marks
        newscore = Scores(user_id = current_user.id , quiz_id = quiz_id , score = total_score , attempt = options_selected ,date_attempted = datetime.now())
        db.session.add(newscore)
        db.session.commit()
        return {"message" : "Quiz Attempted Successfully" , "score" : total_score } , 201


@app.route("/score" , methods=["GET"])
@auth_required("token")
def scores():
    if request.method=="GET":
        if request.args.get("score_id"):
            score_id = request.args.get("score_id")
            score = Scores.query.filter_by(id = score_id , user_id = current_user.id).first()
            if not score:
                return {"message" : "Score not found"} , 404
            quiz = Quiz.query.filter_by(id = score.quiz_id).first()
            quiz_data = {"title" : quiz.title, "id" : quiz.id , "description" : quiz.description,
                         "total_marks" :quiz.total_marks, 
                         } 
            quiz_data["questions"] = []
            for question in quiz.questions:
                quiz_data["questions"].append({"id": question.id , "statement" : question.statement,
                                            "option_a" :question.option_a ,
                                                "option_b" : question.option_b , "option_c" : question.option_c ,
                                                "option_d": question.option_d , "correct_option" : question.correct_option ,
                                                "marks" : question.marks})
            quiz_data["user_attempt"] = score.attempt
            quiz_data["user_score"] = score.score
            return quiz_data , 200  
        else:
            scores = Scores.query.filter_by(user_id = current_user.id).all()
            scores_list = []
            for score in scores:
                quiz = Quiz.query.filter_by(id = score.quiz_id).first()
                scores_list.append({"id" : score.id, "quiz_title" : quiz.title , "score" : score.score , "date_attempted": datetime.strftime(score.date_attempted , "%Y-%m-%d")})
            return scores_list , 200

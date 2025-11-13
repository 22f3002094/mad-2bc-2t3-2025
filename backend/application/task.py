from celery import shared_task
from time import sleep
from .models import db, User, Subject,Role
import csv 
import os
from .utils import prepare_temp
from .mail import send_email

@shared_task(name = "add_together", ignore_result=False)
def add_together(a: int, b: int) -> int:
    sleep(15)
    return a + b



@shared_task(name = "admin_download_csv", ignore_result=False)
def admin_download_csv() :
    admin = Role.query.filter_by(name = "Admin").first().users[0]

    csv_filename = "admin_csv.csv"
    os.makedirs("./static" , exist_ok= True)
    subs = Subject.query.all()
    sleep(15)
    with open(f"./static/{csv_filename}" , "w") as file:

        writerobj = csv.writer(file,delimiter=",")
        writerobj.writerow(["sr.no" , "subject name" , "subject description" , "no of quizzes"])
        for index,sub in enumerate(subs):
            writerobj.writerow([index , sub.name , sub.description , len(sub.quizes)])
    return f"./static/{csv_filename}"



@shared_task(name = "send_admin_monthly_report", ignore_result=False)
def send_admin_monthly_report() :
    admin = Role.query.filter_by(name = "Admin").first().users[0]   
    subs = Subject.query.all()

    data  = {"username" : admin.name , "subjects": subs}
    message = prepare_temp("./templates/adminmail.html" , data)
    send_email(admin.email , "Monthly Activity Report" , message  )
    return "Email sent successfully"
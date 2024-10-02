from django.shortcuts import render,redirect
from django.http import HttpResponse
# from django.contrib.django_settings import setter
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.middleware.AI_chat import AI_ChatBot
from django.contrib.auth.models import User
from .models import chat_bot_User,chat_bot_AI
from datetime import datetime 
from django.db import connection


# Create your views here.
def index(request):
    # setter.set_sql()
    # setter.register_set()

    return render(request, 'index.html')

# FOR TEACHER
def teacher_register(request): #si teacher maka add
    if request.method == "POST":
        username=request.POST['username']
        f_name=request.POST['f_name']
        l_name=request.POST['l_name']
        subject=request.POST['subject']
        password=request.POST['password']
        print(username,f_name,l_name,subject,password)
        user=User.objects.create_user(password=password,username=username)
        create_user=Teachers_db.objects.create(t_student=user,t_first=l_name,t_last=l_name,t_subject=subject)
        create_user.save()
        if user:
            return redirect(login_page)
        
    return render(request, 'loginsignin/authentication-register.html')

def teacher_dashboard(request): #for teacher dashboard
    print(request.user)
    records = chat_bot_User.objects.raw('''
        SELECT edumentor_chat_bot_user.id, edumentor_chat_bot_user.user_chat, 
               edumentor_chat_bot_user.time AS user_time, 
               edumentor_chat_bot_ai.bot_chat, edumentor_chat_bot_ai.time AS ai_time 
        FROM edumentor_chat_bot_user 
        LEFT JOIN edumentor_chat_bot_ai 
        ON edumentor_chat_bot_ai.id = edumentor_chat_bot_user.id
        ORDER BY edumentor_chat_bot_user.time DESC;  
    ''')
   

    if request.method =="POST":
        user_chat=request.POST["user_chat"]

        base_question = """ Your name is Mentor, act as a teacher
    """
        
        user_date = datetime.now()
        chatbot=AI_ChatBot(base_question)
        insert=chat_bot_User.objects.create(base_id=request.user,user_chat=user_chat,time=user_date)
        AI_date = datetime.now()
        insert.save()
        AI_response=chatbot.ask(user_chat)
        insert_AI=chat_bot_AI.objects.create(base_id=request.user,bot_chat=str(AI_response),time=AI_date)
        insert_AI.save()

        records = chat_bot_User.objects.raw('''
        SELECT edumentor_chat_bot_user.id, edumentor_chat_bot_user.user_chat, 
               edumentor_chat_bot_user.time AS user_time, 
               edumentor_chat_bot_ai.bot_chat, edumentor_chat_bot_ai.time AS ai_time 
        FROM edumentor_chat_bot_user 
        LEFT JOIN edumentor_chat_bot_ai 
        ON edumentor_chat_bot_ai.id = edumentor_chat_bot_user.id
        ORDER BY edumentor_chat_bot_user.time DESC;  
    ''')
       
        return render(request, 'dashboard_teacher/dashboard_teacher.html',{"records":records})
        
   
    return render(request, 'dashboard_teacher/dashboard_teacher.html',{"records":records})

def teacher_eroll_student(request):  #for teacher dashboard
    print(request.user)
    if request.method == "POST":
        username=request.POST['s_username']
        f_name=request.POST['s_fname']
        l_name=request.POST['s_lname']
        s_section=request.POST['s_section']
        password=request.POST['s_password']
        user=User.objects.create_user(password=password,username=username)
        create_student=Student_db.objects.create(s_student=user,s_first=f_name,s_last=l_name,section=s_section)
        add_student=T_list_student_db.objects.create(student=create_student,teachers=request.user)
        add_student.save()
        create_student.save()

        if add_student:
            return redirect(teacher_dashboard)

    return render(request, 'dashboard_teacher/blank.html')
  

def teacher_makematerialquiz(request): #diri makaupload pdf materials si teacher kag para mahimo ang quiz
    # return render(request,'')
    pass
# FOR STUDENT

def login_page(request): #student login
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        # print(username,password)
        teacher=authenticate(username=username,password=password)
        if teacher:
            login(request,teacher)
            return redirect(teacher_dashboard)
        else:
            return render(request, 'loginsignin/authentication-login.html')


    return render(request, 'loginsignin/authentication-login.html')


def student_dashboard(request): #for student dashboard ari di si progress
    return render(request,'dashboard_teacher/dashboard_student.html')

def student_quiz(request): # student quiz - muni makita ni student
    # return render(request,'')
    pass



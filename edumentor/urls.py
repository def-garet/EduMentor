from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('register/', views.teacher_register, name="T_register"),
    path('login/', views.login_page, name="login_page"),
    path('teacher-dashboard/', views.teacher_dashboard, name="teacher_dashboard"),
    path('student-dashboard/', views.student_dashboard, name="student_dashboard"),
    path('Eroll_student/', views.teacher_eroll_student, name="add_student"),


    # path('student-quiz/', views.student_quiz, name="student_quiz")
    # path('teacher-materials/', views.teacher_makematerialquiz, name="student_quiz")
]

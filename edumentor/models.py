from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student_db (models.Model):
    id=models.AutoField(primary_key=True)
    s_student=models.OneToOneField(User,on_delete=models.CASCADE)
    s_first=models.CharField(max_length=255,null=False)
    s_last=models.CharField(max_length=255,null=False)
    section=models.CharField(max_length=255,null=False)
    s_profile_pic=models.ImageField(blank=True, null=True)

class Teachers_db(models.Model):
    id=models.AutoField(primary_key=True)
    t_student=models.OneToOneField(User,on_delete=models.CASCADE)
    t_first=models.CharField(max_length=255,null=False)
    t_last=models.CharField(max_length=255,null=False)
    t_subject=models.CharField(max_length=255,null=False)
    t_profile_pic=models.ImageField(blank=True, null=True)

class chat_bot_User (models.Model):
    id=models.AutoField(primary_key=True)
    base_id=models.ForeignKey(User,on_delete=models.CASCADE)
    user_chat=models.CharField(max_length=255)
    time=models.TimeField()

    def __str__(self):
        return self.user_chat

class chat_bot_AI (models.Model):
    id=models.AutoField(primary_key=True)
    base_id=models.ForeignKey(User,on_delete=models.CASCADE)
    bot_chat=models.TextField()
    time=models.TimeField()

class T_list_student_db(models.Model):
    id=models.AutoField(primary_key=True)
    student=models.OneToOneField(Student_db,on_delete=models.CASCADE)
    teachers=models.OneToOneField(User,on_delete=models.CASCADE)

class T_StorageQuizdb(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)

class T_Quiz(models.Model):
    id=models.AutoField(primary_key=True)
    t_quiz_id=models.ForeignKey(T_StorageQuizdb,on_delete=models.CASCADE)
    question=models.TextField()
    answer=models.TextField()


class T_material(models.Model):
    id=models.AutoField(primary_key=True)
    m_name=models.TextField()
    material=models.TextField()

    
class T_student_scoresdb(models.Model):
    id=models.AutoField(primary_key=True)  
    quiz_name=models.ForeignKey(T_StorageQuizdb,on_delete=models.CASCADE)
    name_studnet=models.ForeignKey(T_list_student_db,on_delete=models.CASCADE)
    STD_score=models.IntegerField()


class Student_subject_db(models.Model):
    id=models.AutoField(primary_key=True)
    subject=models.CharField(max_length=255,null=False)
    Teachers_db=models.ForeignKey(Teachers_db,on_delete=models.CASCADE)
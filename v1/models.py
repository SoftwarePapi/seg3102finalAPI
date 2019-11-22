from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your class-based models here.

class Users(models.Model):
    user_id = models.AutoField()
    account_type = models.CharField()
    first_name = models.CharField()
    last_name = models.CharField()
    indentification_number = models.IntegerField()
    program = models.CharField()
    email = models.CharField()
    password = models.CharField()
    #password will not have hashing for now, any kind of auth needs JWT

class Teams(models.Model):
    team_id = models.AutoField()
    team_name = models.CharField()
    creation_date = models.DateTimeField(default=default=datetime.now())
    captain = models.ForeignKey('Users', on_delete=models.CASCADE())
    status = models.CharField()
    min_capacity = models.IntegerField()
    max_capacity = models.IntegerField()

class Team_Members(models.Model):
    id = models.AutoField()
    team_id = models.ForeignKey('Teams', on_delete=models.CASCADE())
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE())

class Courses(models.Model):
    course_id = models.AutoField()
    course_code = models.CharField()

class Sections(models.Model):
    section_id = models.AutoField()
    section_name = models.CharField()
    course_id = models.ForeignKey('Courses', on_delete=models.CASCADE())
    professor = models.ForeignKey('Users', on_delete=models.CASCADE())

class Section_students(models.Model):
    id = models.AutoField()
    section_id = models.ForeignKey('Sections', on_delete=models.CASCADE())
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE())

class Threads(models.Model):
    thread_id = models.AutoField()
    title = models.CharField()
    body_text = models.CharField()
    author = models.ForeignKey('Users', on_delete=models.CASCADE())
    team_id = models.ForeignKey('Teams', on_delete=models.CASCADE())

class Comments(models.Model):
    comment_id = models.AutoField()
    body_text = models.CharField()
    author = models.ForeignKey('Users', on_delete=models.CASCADE())
    thread_id = models.ForeignKey('Threads', on_delete=models.CASCADE())

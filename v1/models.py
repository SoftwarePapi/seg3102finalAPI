from django.db import models
# In case vvv
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your class-based models here.

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    account_type = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    indentification_number = models.IntegerField()
    program = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    #password will not have hashing for now, any kind of auth needs JWT and the django model auth User

class Teams(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True)
    captain = models.ForeignKey('Users', on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    min_capacity = models.IntegerField()
    max_capacity = models.IntegerField()
    section_id = models.ForeignKey('Sections', on_delete=models.CASCADE)

class Team_Members(models.Model):
    id = models.AutoField(primary_key=True)
    team_id = models.ForeignKey('Teams', on_delete=models.CASCADE)
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE)

class Courses(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_code = models.CharField(max_length=255)

class Sections(models.Model):
    section_id = models.AutoField(primary_key=True)
    section_name = models.CharField(max_length=255)
    course_id = models.ForeignKey('Courses', on_delete=models.CASCADE)
    professor = models.ForeignKey('Users', on_delete=models.CASCADE)

class Section_students(models.Model):
    id = models.AutoField(primary_key=True)
    section_id = models.ForeignKey('Sections', on_delete=models.CASCADE)
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE)

class Threads(models.Model):
    thread_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    body_text = models.CharField(max_length=255)
    author = models.ForeignKey('Users', on_delete=models.CASCADE)
    team_id = models.ForeignKey('Teams', on_delete=models.CASCADE)

class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    body_text = models.CharField(max_length=255)
    author = models.ForeignKey('Users', on_delete=models.CASCADE)
    thread_id = models.ForeignKey('Threads', on_delete=models.CASCADE)

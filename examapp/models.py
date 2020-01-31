from django.db import models

# Create your models here.


class Login(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=15)
    user = models.CharField(max_length=15, default='student')


class Reg_Student(models.Model):
    name = models.CharField(max_length=25)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=15)
    login_user = models.ForeignKey(Login, on_delete=models.CASCADE)

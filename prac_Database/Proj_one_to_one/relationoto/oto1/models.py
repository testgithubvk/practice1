from operator import mod
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Page(models.Model):
    puser = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    page_name = models.CharField(max_length=50)
    page_publish_date = models.DateField()

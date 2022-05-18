from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=30, primary_key=True)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=70)
    post_cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    post_publish_date = models.DateField()

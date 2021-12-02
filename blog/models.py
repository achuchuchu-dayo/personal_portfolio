from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    discription = models.TextField(max_length=250)
    date = models.DateField()
   
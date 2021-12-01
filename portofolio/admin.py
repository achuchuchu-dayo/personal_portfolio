from django.contrib import admin
from .models import Project
#Adminのサイトで表示させたいクラスを書く
admin.site.register(Project)

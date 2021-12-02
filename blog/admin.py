from django.contrib import admin
from .models import Blog
#Adminのサイトで表示させたいクラスを書く
admin.site.register(Blog)

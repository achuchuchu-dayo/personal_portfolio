from django.shortcuts import render
from .models import Blog

# Create your views here.
def all_blogs(request):
    return render(request, 'blog/blog.html')
# Create your views here.

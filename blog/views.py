from django.shortcuts import render
from .models import Blog

# Create your views here.
def all_blogs(request):
    blogs = Blog.objects.order_by("-date")[:3]
    return render(request, 'blog/blog.html', {'blogs':blogs})
# Create your views here.

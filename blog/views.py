from django.shortcuts import render
# from django.http import HttpResponse
from .models import Blog

def allblogs(request):
  blogs = Blog.Objects
  return render(request, 'blog/allblogs.html', {'blogs':blogs})


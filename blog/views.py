from django.shortcuts import render, get_object_or_404 #either get the object or get 404 page
# from django.http import HttpResponse
from .models import Blog

def allblogs(request):
  blogs = Blog.objects
  return render(request, 'blog/allblogs.html', {'blogs':blogs})

def detail(request, blog_id):
  detailblog = get_object_or_404(Blog, pk=blog_id)
  return render(request, 'blog/detail.html', {'blog':detailblog})



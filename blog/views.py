from django.shortcuts import render
from django.http import HttpResponse

from . import views

def allblogs(request):
  return render(request, 'blog/allblogs.html')

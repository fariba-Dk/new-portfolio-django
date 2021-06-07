from django.shortcuts import render
# from django.http import HttpResponse


# get the jobs here then send them to render

from .models import Jobs
def home(request):
    return render(request, 'jobs/home.html', {'jobs':jobs})

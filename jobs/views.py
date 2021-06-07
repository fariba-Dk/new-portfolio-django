from django.shortcuts import render
# from django.http import HttpResponse

from .models import Job
def home(request):
    return render(request, 'jobs/home.html', {'jobs':jobs})

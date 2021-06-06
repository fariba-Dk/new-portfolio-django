from django.shortcuts import render


from django.http import HttpResponse


#views methods always take req as first arg
def home(request):
    return HttpResponse("Hello World!")

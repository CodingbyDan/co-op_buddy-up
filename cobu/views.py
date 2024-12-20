# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("Hello World! Can you see me?")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("This is my about page!")
    return render(request, 'about.html')
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')

def research(request):
    return render(request,'research.html')
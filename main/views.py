#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    return render(request,'main/home_page.html',{})

def about_page(request):
    return render(request,'main/about.html',{})

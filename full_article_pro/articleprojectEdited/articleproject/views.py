from django .http import HttpResponse
from django.shortcuts import render




def home(request):
    # return HttpResponse('Home')
    return render(request,'home.html')

def about(request):
    # return HttpResponse('about')
    return render(request,'about.html')

def home1(request):
    return render(request,'home1.html')
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login,logout

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.
def signup_view(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #log the user in
            return redirect('article_for_listsare:list')
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'forms_are':form})


def login_view(request):
    if request.method=='POST':
       form = AuthenticationForm(data=request.POST)
       if form.is_valid():
           user = form.get_user()
           login(request,user)
           return redirect('article_for_listsare:list')
       #log in the user 
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'forms_are':form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('article_for_listsare:list')
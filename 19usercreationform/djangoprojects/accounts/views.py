from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def signup_view(request):
    form = UserCreationForm()
    return render(request,'accounts/signup.html',{'forms_are':form})
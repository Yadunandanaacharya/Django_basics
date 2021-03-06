from django.shortcuts import render, redirect 
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms

# Create your views here.
def article_list(request):
    article_for_list = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html',{'article_for_listsare':article_for_list})
def article_detail(request,slug):
    # return HttpResponse(slug)
    article_for_detail = Article.objects.get(slug = slug)
    return render(request,'articles/article_detail.html',{'article_details': article_for_detail}) 

@login_required(login_url="/accounts/login")
def  article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            #save to db
            instance  = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('article_for_listsare:list')

    form = forms.CreateArticle()
    return render(request,'articles/article_create.html',{'Myforms':form})
    
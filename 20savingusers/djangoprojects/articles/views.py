from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
# Create your views here.
def article_list(request):
    article_for_list = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html',{'article_for_listsare':article_for_list})
def article_detail(request,slug):
    # return HttpResponse(slug)
    article_for_detail = Article.objects.get(slug = slug)
    return render(request,'articles/article_detail.html',{'article_details': article_for_detail}) 
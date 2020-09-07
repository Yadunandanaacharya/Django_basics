from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
# Create your views here.
def article_list(request):
    article1 = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html',{'art':article1})

def article_detail(request,slug):
    return HttpResponse(slug)
from django.shortcuts import render
from .models import Article
# Create your views here.
def article_list(request):
    article = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html',{'artticles':article})
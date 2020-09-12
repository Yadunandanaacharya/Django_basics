from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'article_for_listsare'
# app_name = 'articles'#_for_listsare'

urlpatterns = [
    url(r'^$', views.article_list,name='list'),
    url(r'^(?P<slug>[\w-]+)/$',views.article_detail, name='detail'),
]

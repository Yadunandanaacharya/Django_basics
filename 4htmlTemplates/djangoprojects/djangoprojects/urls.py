from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', views.about),
    url(r'^$', views.homepage),
]

# Important: url(r'^$', views.homepage), this is wrong $ used at end to
# check or match for ending characters
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)
    thumbnail = models.ImageField(default='default.png',blank = True)
    author = models.ForeignKey(User, default=1,verbose_name='Author', on_delete=models.SET_DEFAULT)

    # author
    # add thumbanil later

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:60] + '...'

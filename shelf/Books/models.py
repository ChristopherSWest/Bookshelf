from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=64,unique=True)
    title = models.CharField(max_length=64, null=True)
    owner = models.ManyToManyField(get_user_model())
    author = models.CharField(max_length=64, null=True)
    cover_url = models.CharField(max_length=64, null=True)
    publisher = models.CharField(max_length=64, null=True)
    published_date = models.CharField(max_length=64, null=True)
    subjects = models.TextField(null=True)
    added_date = models.DateTimeField(auto_now_add=True)
    most_recent_added_dt = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    
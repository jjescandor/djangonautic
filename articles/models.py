from logging.handlers import SYSLOG_UDP_PORT
from sre_constants import SRE_FLAG_DEBUG
from turtle import title
from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    # add in thumbnail later
    # add in author later


# Commands to make models
# python manage.py makemigrations
# python manage.py migrate

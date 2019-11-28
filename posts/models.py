from django.db import models
from rest_framework import serializers
# Create your models here.

class posts(models.Model):
    userid = models.IntegerField()
    comment = models.CharField(max_length=200)
    username = models.CharField(max_length=20, default='ss')
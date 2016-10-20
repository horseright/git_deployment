from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Blog(models.Model):
      title = models.CharField(max_length=100, default="1st blog")
      blog = models.TextField(max_length=1000, default="1st blog")
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
      comment = models.TextField(max_length=1000, default="1st comment")
      blog = models.ForeignKey(Blog, default=1)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)

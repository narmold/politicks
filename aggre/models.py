from __future__ import unicode_literals

from django.db import models

# Create your models here.
class posts(models.Model):
    source = models.CharField(max_length = 30)
    source_url = models.TextField()
    title = models.CharField(max_length = 100)
    uri = models.CharField(max_length=20)
    summary = models.TextField()
    location = models.CharField(max_length = 30)
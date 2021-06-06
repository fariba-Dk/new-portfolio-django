from django.db import models


# Create your models here.
class Job(models.Model):
  image = models.ImageField(upload_to='images/')
  summary = models.CharField(max_length=200)

class Document(models.Model):
  title = models.CharField(max_length=128, blank=True)
  file = models.FileField(upload_to='documents', max_length=200)

from django.db import models

# Create your models here.

class Services(models.Model):
    name = models.CharField(max_length=100)
    detail=models.CharField(max_length=100)

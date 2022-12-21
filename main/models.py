from django.db import models


# Create your models here.

class GeneralInfo(models.Model):
    target = models.CharField(max_length=50)
    target_link = models.URLField(max_length=300, blank=True, null=True)
    programmer = models.CharField(max_length=50)
    programmer_link = models.URLField(max_length=300, blank=True, null=True)
    text = models.TextField(max_length=200)

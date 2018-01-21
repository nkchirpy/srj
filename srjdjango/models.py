from django.db import models

# Create your models here.

class Wellsaid(models.Model):

    name = models.CharField(max_length=255, blank=True)
    fetch_image = models.FileField(upload_to='documents/')
    description = models.CharField(max_length=500, blank=True)

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Wellsaid(models.Model):

    name = models.CharField(max_length=255, blank=True)
    fetch_image = models.FileField(upload_to='documents/')
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name


class Enquirymodel(models.Model):

    name = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=200)
    contact_number = models.CharField(max_length=215)
    comments = models.CharField(max_length=1000)
    # browse = models.FileField(upload_to='enquiry/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


    def __str__(self):
        return self.name

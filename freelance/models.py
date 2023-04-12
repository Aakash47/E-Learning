from django.db import models
from store.models import Customer
from datetime import datetime

# Create your models here.

class Freelance(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True, help_text='This field should be unique')
    title = models.CharField(max_length=100, null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True,upload_to = "thumbnail")
    description = models.TextField(null=True, blank=True)
    

    def __str__(self):
        return self.title

    @property
    def thumbnailURL(self):
    	try:
    		url = self.thumbnail.url
    	except:
    		url = ''
    	return url

class Projects(models.Model):
    skills = models.CharField(max_length=100, null=True, blank=True)
    projects_done = models.TextField(max_length=100, null=True, blank=True)
    # Projects_links = models.URLField(max_length=100, null=True, blank=True)
    freelance = models.ForeignKey(Freelance, null=False, on_delete=models.CASCADE)


class Fcontact(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    freelance = models.ForeignKey(Freelance, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    budget = models.IntegerField()
    contact_no = models.IntegerField()

    def __str__(self):
        return str(self.freelance.title)
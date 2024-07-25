from django.db import models
from django.utils import timezone

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100)
    video_url = models.URLField(max_length=200)  # Store the video URL
    thumbnails = models.ImageField(upload_to='media')
    date = models.DateField(default=timezone.now)
    description = models.TextField(null=True, blank=True, default='')
    
    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title

class Upcoming_video(models.Model):
    title = models.CharField(max_length=100,default=None)
    trailer_url = models.URLField(max_length=200, default=None)
    thumbnails = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title
    
class Team(models.Model):
    name = models.CharField(max_length=100,default=None)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name
    
class Authorities(models.Model): 
    name = models.CharField(max_length=100,default=None)
    role = models.CharField(max_length=100,default=None)
    image = models.ImageField(upload_to='media')

    class Meta:
        verbose_name_plural = 'authorities'

    def __str__(self):
        return self.name    




        
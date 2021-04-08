from django.db import models

class Video(models.Model):
    video = models.CharField(max_length=1000)

# Create your models here.

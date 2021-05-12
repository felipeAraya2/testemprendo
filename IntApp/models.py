from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Curso(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    profesor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True,null=True)

    def __str__(self):
        return self.nombre

class Video(models.Model):
    video = models.CharField(max_length=1000)
    nombre = models.CharField(max_length=200)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)


# Create your models here.
    
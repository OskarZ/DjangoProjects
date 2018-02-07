

# Create your models here.

from django.db import models
from django.utils import timezone


class Post(models.Model):

    Categorys = (
        ('Reisen','Reisen'),
        ('Arbeit','Arbeit'),
        ('Freizeit','Freizeit'),
        ('Andere','Andere'),
    )
    title = models.CharField(max_length=200)
    text = models.TextField()
    category = models.CharField(max_length=200, choices=Categorys, default='Andere')
    created_date = models.DateTimeField(
            default=timezone.now)


class Mail(models.Model):
    mail = models.CharField(max_length=40)
    title = models.CharField(max_length=50, default='Kein Titel')
    nachricht = models.TextField()

class account(models.Model):
    adresse = models.CharField(max_length=40)
    passwort = models.CharField(max_length=20)

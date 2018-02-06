

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



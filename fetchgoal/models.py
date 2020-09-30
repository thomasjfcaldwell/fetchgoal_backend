from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)

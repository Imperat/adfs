from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    team = models.CharField(max_length=50)
    link = models.CharField(max_length=60)
    goals = models.IntegerField()

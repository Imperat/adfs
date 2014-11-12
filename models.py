
import os
from os.path import abspath, dirname
import sys
# Set up django
project_dir = abspath(dirname(dirname(__file__)))
sys.path.insert(0, project_dir)
os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"
from django.db import models
class Person(models.Model):
    name = models.CharField(max_length=30)
    team = models.CharField(max_length=50)
    link = models.CharField(max_length=60)
    goals = models.IntegerField()

class Match(models.Model):
    team1 = models.CharField(max_length=30)
    team2 = models.CharField(max_length=50)
    goal1 = models.IntegerField()
    goal2 = models.IntegerField()
    group = models.CharField(max_length=50)
    tour = models.CharField(max_length=50)
    play = models.CharField(max_length=1)
    date = models.CharField(max_length=50)


from django.contrib import admin

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'team')
admin.site.register(Person, PersonAdmin)

class MatchAdmin(admin.ModelAdmin):
    list_display = ('team1', 'team2','goal1', 'goal2', 'tour')
admin.site.register(Match, MatchAdmin)
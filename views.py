# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template.loader import render_to_string
from adfs.models import Person, Match

class player:
    def __init__ (self, team,name,goals,link):
        self.name=name
        self.team=team
        self.goals=goals
        self.link=link

b = Person(name="Михаил Лелякин", team="Пыльник", goals=2, link="Imperator")
#b.save(force_insert=True)




def calend(request):
    lst=[]
    for i in Person.objects.all():
        lst.append(player(i.team,i.name, i.goals, i.link))
    pl = []
    for i in Match.objects.all():
        pl.append(i)
    lst.sort(key=lambda x: x.goals)
    lst.reverse()
    rendered = render_to_string('calend.html', { 'playerlist': lst, 'matchs':pl, 'gr':'all' })
    return HttpResponse(rendered)


def hello(request):
    lst=[]
    for i in Person.objects.all():
        lst.append(player(i.team,i.name, i.goals, i.link))
    lst.sort(key=lambda x: x.goals)
    lst.reverse()
    rendered = render_to_string('main.html', { 'playerlist': lst })
    return HttpResponse(rendered)

def stat(request):
    lst=[]

    for i in Person.objects.all():
        lst.append(player(i.team,i.name, i.goals, i.link))
    lst.sort(key=lambda x: x.goals)
    lst.reverse()
    rendered = render_to_string('statistic.html', { 'playerlist': lst })
    return HttpResponse(rendered)

def boms(request):
    lst=[]
    for i in Person.objects.all():
        lst.append(player(i.team,i.name, i.goals, i.link))
    lst.sort(key=lambda x: x.goals)
    lst.reverse()
    rendered = render_to_string('bombardiers.html', { 'playerlist': [], 'liste' : lst })
    return HttpResponse(rendered)
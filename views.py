# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template.loader import render_to_string
from adfs.models import Person, Match
from PIL import Image, ImageDraw, ImageFont
text = "Hello, Rasim!!!"
color = (0, 0, 120)
img = Image.new('RGB', (100, 50), color)
imgDrawer = ImageDraw.Draw(img)
imgDrawer.text((10, 20), text)
img.save("/home/michaill/adfs/pil-basic-example.png")

def create_image():
    for j in "ABCD":
        img = Image.open('/home/michaill/adfs/media/table.png')
        font = ImageFont.truetype("/home/michaill/adfs/media/arial.ttf",15, encoding = "unic")
        draw = ImageDraw.Draw(img)
        k = 30
        draw.text((43,10), u"Группа " + j, fill="black", font = font)
        for i in filter(lambda x: x[1].gr == j, infon()):
            draw.text((50,k), i[0], fill="black", font = font)
            draw.text((285,k), str(i[1].playes), fill="black", font = font)
            draw.text((330,k), str(i[1].v), fill="black", font = font)
            draw.text((375,k), str(i[1].n), fill="black", font = font)
            draw.text((420,k), str(i[1].p), fill="black", font = font)
            draw.text((465,k), str(i[1].golsab), fill="black", font = font)
            draw.text((510,k), str(i[1].golprop), fill="black", font = font)
            draw.text((555,k), str(i[1].point()), fill="black", font = font)
            k+=26
        img.save('/home/michaill/adfs/static/table'+ j + '.png', 'PNG')

f = open ("rasim.txt", "w")
f.write("Rasim")
f.close()


class player:
    def __init__ (self, team,name,goals,link):
        self.name=name
        self.team=team
        self.goals=goals
        self.link=link

b = Person(name="Михаил Лелякин", team="Пыльник", goals=2, link="Imperator")
#b.save(force_insert=True)



class RecOfTeam:
    def __init__ (self):
    	self.name = "Lool"
        self.playes  = 0
        self.v       = 0
        self.n       = 0
        self.p       = 0
        self.golprop = 0
        self.golsab  = 0
        self.gr = 'E'

    def point (self):
        return self.v*3 + self.n

    def rasn (self):
        return self.golsab - self.golprop

    def __lt__ (self,other):
        if self.point() < other.point():
            return True
        elif self.point() == other.point():
            if retMatch(self.name, other.name) == 0:
                if self.rasn() < other.rasn():
                    return True
                else:
                    return False
            if retMatch(self.name, other.name) == True:
                return True
            elif retMatch(self.name, other.name) == -1:
                if self.rasn() < other.rasn():
                    return True
                else:
                    return False
            else:
                return False
    def __gt__(self, other):
        if self.__lt__(other) == False:
            return True
        else:
            return False


def retMatch(team1, team2):
    global t
    global dencity
    for i in Match.objects.all():
        if i.team1 == team1 and i.team2 == team2:
            t = i
            dencity = True
            break
        elif i.team2 == team1 and i.team1 == team2:
            t = i
            dencity = False
            break

    if t.play == 'n':
        return 0
    else:
        if i.goal1 > i.goal2:
            return True ^ dencity
        elif i.goal1 < i.goal2:
            return False ^ dencity
        else:
            return -1

def infon ():
    l = dict()
    for i in Match.objects.all():
        if i.play == 'n':
            if i.team1 not in l.keys():
                t = RecOfTeam()
                t.gr = i.group
                t.name = i.team1
                l[i.team1] = t
        if i.play == 'y':
            if i.team1 in l.keys():
                t = l[i.team1]
                # Hier must be function: take 't' and 'i', return new t.
                t.playes = t.playes + 1
                t.golsab = t.golsab + i.goal1
                t.golprop = t.golprop + i.goal2
                if i.goal1 > i.goal2:
                   t.v = t.v + 1
                elif i.goal1 < i.goal2:
                    t.p = t.p + 1
                else:
                    t.n = t.n + 1
                # End of this function
                l[i.team1] = t
            else:
                l[i.team1] = RecOfTeam()
                l[i.team1].gr = i.group
                t = l[i.team1]
                t.playes = t.playes + 1
                t.golsab = t.golsab + i.goal1
                t.golprop = t.golprop + i.goal2
                if i.goal1 > i.goal2:
                    t.v = t.v + 1
                elif i.goal1 < i.goal2:
                    t.p = t.p + 1
                else:
                    t.n = t.n + 1
                t.name = i.team1
                l[i.team1] = t
           #Индусский код. В ближайшее время точно переделать стоит его!
            if i.team2 in l.keys():
                t = l[i.team2]
                t.playes = t.playes + 1
                t.golsab = t.golsab + i.goal2
                t.golprop = t.golprop + i.goal1
                if i.goal1 > i.goal2:
                    t.p = t.p + 1
                elif i.goal1 < i.goal2:
                    t.v = t.v + 1
                else:
                    t.n = t.n + 1
                l[i.team2] = t
            else:
                l[i.team2] = RecOfTeam()
                l[i.team2].gr = i.group
                t = l[i.team2]
                t.playes = t.playes + 1
                t.golsab = t.golsab + i.goal2
                t.golprop = t.golprop + i.goal1
                if i.goal1 > i.goal2:
                    t.p = t.p + 1
                elif i.goal1 < i.goal2:
                    t.v = t.v + 1
                else:
                  t.n = t.n + 1
                t.name = i.team2
                l[i.team2] = t
    #О-хо-хо

    info = l.items()
    info.sort(key = lambda x: x[1])
    info.reverse()
    return info

def playerList (k=0):
    lst=[]
    for i in Person.objects.all():
        lst.append(player(i.team,i.name, i.goals, i.link))
    lst.sort(key=lambda x: x.goals)
    lst.reverse()
    if k==0:
        return lst
    else:
        return lst[:k]

def calend(request, group,tour):
    pl = []
    for i in Match.objects.all():
        pl.append(i)
    if group in "ABCD":
        pl = list(filter(lambda x: x.group == group, pl))
    else:
        pass
    if int(tour) in range(6):
            pl = list(filter(lambda x: x.tour == tour, pl))
    else:
        pass
    pl.sort(key=lambda x: x.tour)
    rendered = render_to_string('calend.html', { 'playerlist': playerList(5), 'matchs':pl, 'gr':group, 'tr':tour})
    return HttpResponse(rendered)


def hello(request):
    rendered = render_to_string('main.html', { 'playerlist': playerList(5) })
    return HttpResponse(rendered)

def stat(request):
    create_image()
    rendered = render_to_string('statistic.html', { 'playerlist': playerList(5), 'info':infon()})
    return HttpResponse(rendered)

def boms(request):
    rendered = render_to_string('bombardiers.html', { 'playerlist': [], 'liste' : playerList(0) })
    return HttpResponse(rendered)

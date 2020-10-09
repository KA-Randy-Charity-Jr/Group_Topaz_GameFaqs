from django.shortcuts import render
from game_app.models import Game
from gamefaq_app.models import GameFaq
from news_app.models import Newspost

# Create your views here.
def  gamesview(request,gameid):
    g = Game.objects.get(id=gameid)
    f = GameFaq.objects.filter(game=g.id)
    n = Newspost.objects.filter(game=g.id)
    c = g.consoles.all()

    return render(request,"games.html",{"f":f,"g":g,"n":n,"c":c})
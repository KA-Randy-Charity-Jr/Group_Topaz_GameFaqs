from django.shortcuts import render
from home.models import Game, Gamefaq

# Create your views here.
def index(request):
    my_games = Game.objects.all()
    return render(request, "index.html", {'game': my_games} )



def post_detail(request, post_id):
    my_game = Game.objects.filter(id=post_id).first()
    gamefaqs = Gamefaq.objects.filter(game=my_game.id)
    return render(request, "game_detail.html", {"post": my_game, "faqs": gamefaqs})
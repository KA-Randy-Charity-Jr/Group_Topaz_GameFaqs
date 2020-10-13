from django.shortcuts import render
from gamefaq_app.models import GameFaq
from gamefaq_app.forms import NewGamefaq
from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from game_app.models import Game
from console_app.models import Console


# Create your views here.
def gamefaqview(request,gamefaqid):
    f= GameFaq.objects.filter(id=gamefaqid)
    return render(request, "gamefaq.html", {"f": f})

def indexview(request):
    f = Game.objects.all()
    return render(request, "index.html", {"f": f})

def newgamefaqview(request):
    f = NewGamefaq()
    if request.method == "POST":
        form = NewGamefaq(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            GameFaq.objects.create(
                title=data.get('title'),
                game=data.get('game'),
                body=data.get('body'),
                difficulty=data.get('difficulty'),author=(request.user))
            return HttpResponseRedirect(reverse('home'))    
    return render (request,"form.html",{"f":f})    

from django.shortcuts import render
from console_app.models import Console
from game_app.models import Game

# Create your views here.


def PlaystationView(request):
    theconsoles = Console.objects.filter(brand="PLAYSTATION").order_by("-id")
    return render(request, "playstation.html", {"consoles": theconsoles})


def XboxView(request):
    theconsoles = Console.objects.filter(brand="XBOX").order_by("-id")
    return render(request, "xbox.html", {"consoles": theconsoles})


def NintendoView(request):
    theconsoles = Console.objects.filter(brand="NINTENDO").order_by("-id")
    return render(request, "nintendo.html", {"consoles": theconsoles})


def PcView(request):
    theconsoles = Console.objects.filter(brand="PC").order_by("-id")
    return render(request, "pc.html", {"consoles": theconsoles})


def consoleview(request, console_id):
    isfavorite = False
    console = Console.objects.get(id=console_id)
    thegames = Game.objects.filter(consoles=console_id).order_by("-id")
    if request.user.is_authenticated:
        if console in request.user.preferred_systems.all():
            isfavorite = True
    return render(request, "console.html", {"console": console, "games": thegames, "isfavorite": isfavorite})

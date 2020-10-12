from django.shortcuts import render
from console_app.models import Console
from game_app.models import Game

# Create your views here.

def PlaystationView(request):
    theconsoles = Console.objects.filter(brand="PLAYSTATION")
    return render(request, "playstation.html", {"consoles": theconsoles})
    
def XboxView(request):
    theconsoles = Console.objects.filter(brand="XBOX")
    return render(request, "xbox.html", {"consoles": theconsoles})
    
def NintendoView(request):
    theconsoles = Console.objects.filter(brand="NINTENDO")
    return render(request, "nintendo.html", {"consoles": theconsoles})

def PcView(request):
    theconsoles = Console.objects.filter(brand="PC")
    return render(request, "pc.html", {"consoles": theconsoles})
    
def consoleview(request, console_id):
    console = Console.objects.get(id=console_id)
    thegames = Game.objects.filter(consoles=console_id)
    return render(request,"console.html",{"console":console,"games":thegames})
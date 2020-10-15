from django.shortcuts import render
from django.template import RequestContext
from gamefaq_app.models import GameFaq
from gamefaq_app.forms import NewGamefaq
from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from django.views.generic import TemplateView, ListView
from django.db.models import Q 
from news_app.models import Newspost
from reviews_app.models import Review
from game_app.models import Game

# Create your views here.
def gamefaqview(request,gamefaqid):
    f = GameFaq.objects.filter(id=gamefaqid)
    c = Review.objects.filter(gamefaq=gamefaqid)
    r = c.count()
    return render(request, "gamefaq.html", {"f": f,"r":r})
    

def indexview(request):
    f = Game.objects.all().order_by("-id")
    n = Newspost.objects.all().order_by("-id")
    return render(request, "index.html", {"f": f,"n":n})

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
                difficulty=data.get('difficulty'), author=(request.user),
                ptype=data.get('ptype'))
            return HttpResponseRedirect(reverse('home'))    
    return render(request, "form.html", {"f": f})


def handler404(request, *args, **argv):
    return render(request, '404.html', status=404)

def handler500(request, *args, **argv):
    return render(request, '500.html', status=500)

class SearchResultsView(ListView):
    model = Game
    template_name = 'search_results.html'
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Game.objects.filter(
            Q(title__icontains=query) 
        )
        return object_list



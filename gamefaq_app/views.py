from django.shortcuts import render
from gamefaq_app.models import GameFaq
from gamefaq_app.forms import NewGamefaq
from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from game_app.models import Game
from django.views.generic import TemplateView, ListView
from django.db.models import Q 
from news_app.models import Newspost

# Create your views here.
def gamefaqview(request,gamefaqid):
    f= GameFaq.objects.filter(id=gamefaqid)
    return render(request, "gamefaq.html", {"f": f})
    

def indexview(request):
    f = Game.objects.all()
    n = Newspost.objects.all()
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
                difficulty=data.get('difficulty'),author=(request.user))
            return HttpResponseRedirect(reverse('home'))    
    return render(request, "form.html", {"f": f})



class SearchResultsView(ListView):
    model = GameFaq
    template_name = 'search_results.html'
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = GameFaq.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )
        return object_list



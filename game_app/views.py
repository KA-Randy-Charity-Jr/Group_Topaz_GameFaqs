from django.shortcuts import render
from game_app.models import Game
from gamefaq_app.models import GameFaq
from news_app.models import Newspost
from django.views.generic import ListView

# Create your views here.


def gamesview(request, gameid):
    isfavorite = False
    g = Game.objects.get(id=gameid)
    f = GameFaq.objects.filter(game=g.id)
    n = Newspost.objects.filter(game=g.id)
    c = g.consoles.all()
    if request.user.is_authenticated:
        if g in request.user.favorited_games.all():
            isfavorite = True

    return render(request, "games.html", {"f": f, "g": g, "n": n, "c": c, "isfavorite": isfavorite})

# class SearchView(ListView):
#     model = Game
#     template_name = 'search_result.html'
#     context_object_name = 'all_search_results'

#     def get_queryset(self):
#        result = super(SearchView, self).get_queryset()
#        query = self.request.GET.get('search')
#        if query:
#           postresult = Game.objects.filter(title__contains=query)
#           result = postresult
#        else:
#            result = None
#        return result


def article_overview(request):
    search_term = ''
    search_term = request.GET['search']
    game = Game.objects.filter(title__icontains=search_term)

    return render(request, 'search_result.html', {'all_search_results': game})

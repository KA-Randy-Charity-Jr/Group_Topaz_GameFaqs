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
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView

# Create your views here.


def gamefaqview(request, gamefaqid):
    f = GameFaq.objects.filter(id=gamefaqid)
    c = Review.objects.filter(gamefaq=gamefaqid)
    r = c.count()
    return render(request, "gamefaq.html", {"f": f, "r": r})


def indexview(request):
    i = 0
    p = 0
    j = 0
    recentgames = []
    recentnews = []
    recentfaqs = []
    f = Game.objects.all().order_by("-id")
    for game in f:
        if i < 20:
            recentgames.append(game)
            i += 1

    n = Newspost.objects.all().order_by("-id")
    for news in n:
        if p < 20:
            recentnews.append(news)
            p += 1
    g = GameFaq.objects.all().order_by("-id")
    for faq in g:
        if j < 20:
            recentfaqs.append(faq)
            j += 1
    return render(request, "index.html", {"f": recentgames, "n": recentnews, "g": recentfaqs})


@login_required
def newgamefaqview(request, gameid):
    g = Game.objects.get(id=gameid)
    f = NewGamefaq()
    if request.method == "POST":
        form = NewGamefaq(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            GameFaq.objects.create(
                title=data.get('title'),
                game=g,
                body=data.get('body'),
                difficulty=data.get('difficulty'), author=(request.user),
                ptype=data.get('ptype'), consoles=data.get('console')),
            return HttpResponseRedirect(reverse('home'))
    return render(request, "form.html", {"f": f})


def handler404(request, *args, **argv):
    return render(request, '404.html', status=404)


def handler500(request, *args, **argv):
    return render(request, '500.html', status=500)


class SearchResultsView(ListView):
    model = Game
    template_name = 'search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = Game.objects.filter(
            Q(title__icontains=query)
        )
        return object_list


class FaqResultsView(ListView):
    model = GameFaq
    template_name = 'search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = GameFaq.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )
        return object_list


class Edit_GamefaqView(LoginRequiredMixin, TemplateView):
    def get(self, request, faqid):
        faq = GameFaq.objects.get(id=faqid)
        if request.user.id == faq.author.id:
            data = {
                "title": faq.title,
                "body": faq.body,

            }
            f = NewGamefaq(initial=data)
            return render(request, "form.html", {"f": f})
        else:
            return HttpResponseRedirect(reverse('home'))

    def post(self, request, faqid):
        faq = GameFaq.objects.get(id=faqid)
        if request.method == "POST":
            form = NewGamefaq(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                faq.title = data["title"]
                faq.body = data["body"]
                faq.difficulty = data["difficulty"]
                faq.ptype = data["ptype"]
                faq.save()
                return HttpResponseRedirect(f"/gamefaq/{faqid}/")


class Deletefaq(DeleteView):
    model = GameFaq
    template_name = "delete.html"
    success_url = "/"


class ActivityFeed(LoginRequiredMixin, TemplateView):
    def get(self, request):
        feedfaqs = []
        feednews = []
        i = 0
        n = 0
        q = 0
        faqs = GameFaq.objects.all().order_by("-id")
        for faq in faqs:
            if i < 20:
                followers = faq.author.followers.all()
                for follow in followers:
                    if request.user.username == follow.username:
                        feedfaqs.append(faq)
                        i += 1
        newsposts = Newspost.objects.all().order_by("-id")
        for post in newsposts:
            if n < 20:
                nfollowers = post.author.followers.all()
                for follow in nfollowers:
                    if request.user.username == follow.username:
                        feednews.append(post)
                        n += 1

        return render(request, "feed.html", {"faqs": feedfaqs, "news": feednews})

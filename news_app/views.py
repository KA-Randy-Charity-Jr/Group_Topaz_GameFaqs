from django.shortcuts import render
from django.views.generic import TemplateView
from news_app.forms import NewNewspost
from news_app.models import Newspost
from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from game_app.models import Game
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView

# Create your views here.


class Newspostform(LoginRequiredMixin, TemplateView):
    def get(self, request, gameid):
        f = NewNewspost()
        game = Game.objects.get(id=gameid)
        return render(request, "form.html", {"f": f})

    def post(self, request, gameid):
        if request.method == "POST":
            form = NewNewspost(request.POST)
            game = Game.objects.get(id=gameid)
            if form.is_valid():
                data = form.cleaned_data
                Newspost.objects.create(
                    title=data.get('title'),
                    body=data.get('body'),
                    author=request.user,
                    game=game
                )

                return HttpResponseRedirect(f"/game/{gameid}")


def NewpostView(request, newsid):
    post = Newspost.objects.get(id=newsid)
    return render(request, "newspost.html", {"post": post})


class Edit_NewsView(LoginRequiredMixin, TemplateView):
    def get(self, request, newsid):
        post = Newspost.objects.get(id=newsid)
        if request.user.id == post.author.id:
            data = {
                "title": post.title,
                "body": post.body,

            }
            f = NewNewspost(initial=data)
            return render(request, "form.html", {"f": f})
        else:
            return HttpResponseRedirect(reverse('home'))

    def post(self, request, newsid):
        post = Newspost.objects.get(id=newsid)
        if request.method == "POST":
            form = NewNewspost(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                post.title = data["title"]
                post.body = data["body"]

                post.save()
                return HttpResponseRedirect(f'/newspost/{newsid}')


class DeleteNews(DeleteView):
    model = Newspost
    template_name = "delete.html"
    success_url = "/"

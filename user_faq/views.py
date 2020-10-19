from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from user_faq.forms import GamefaqUserForm, CommentForm
from authentication.views import login_view
from user_faq.models import GamefaqUser, User_Comments
from user_faq.forms import SignupForm
from gamefaq_app.models import GameFaq
from game_app.models import Game
from console_app.models import Console
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView

# Create your views here.


def index(request):
    return render(request, "index.html")


class signup_view(TemplateView):
    def get(self, request):
        form = SignupForm()
        return render(request, 'basic.html', {"form": form})

    def post(self, request):
        if request.method == "POST":
            form = SignupForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                new_user = GamefaqUser.objects.create_user(
                    displayname=data.get("displayname"),
                    bio=data.get("bio"),
                    username=data.get("username"),
                    password=data.get("password"),
                )
                login(request, new_user)
                return HttpResponseRedirect(reverse('home'))


def user_profile_view(request, user_id):
    recentcomments = []
    i = 0
    isfollow = False
    html = 'user_profile.html'
    user_detail = GamefaqUser.objects.filter(id=user_id).first()
    f = GameFaq.objects.filter(author=user_id)
    g = GamefaqUser.objects.get(id=user_id)
    comments = User_Comments.objects.filter(touser=user_id).order_by("-id")
    consoles = g.preferred_systems.all()
    games = g.favorited_games.all()
    followers = g.followers.all()
    for comment in comments:
        if i < 20:
            recentcomments.append(comment)
            i += 1
    if request.user in g.followers.all():
        isfollow = True
    return render(request, html, {'profile': user_detail, "f": f, "isfollow": isfollow, "comments": recentcomments, "consoles": consoles, "games": games, "followers": followers})


class edit_user_profile_view(LoginRequiredMixin, TemplateView):
    def get(self, request, user_id):
        faq_user = GamefaqUser.objects.get(id=user_id)
        data = {
            "displayname": faq_user.displayname,
            "bio": faq_user.bio,
            "email": faq_user.email
        }
        form = GamefaqUserForm(initial=data)
        return render(request, "edit_form.html", {"form": form})

    def post(self, request, user_id):
        faq_user = GamefaqUser.objects.get(id=user_id)
        if request.method == "POST":
            form = GamefaqUserForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                faq_user.displayname = data["displayname"]
                faq_user.bio = data["bio"]
                faq_user.email = data["email"]
                faq_user.save()
                return HttpResponseRedirect(reverse('user_profile', args=[faq_user.id]))


class FollowView(LoginRequiredMixin, TemplateView):
    def get(self, request, userid):
        theuser = GamefaqUser.objects.get(id=userid)
        theuser.followers.add(request.user)
        theuser.save()
        return HttpResponseRedirect(f"/user_profile_view/{userid}")


class UnFollowView(LoginRequiredMixin, TemplateView):
    def get(self, request, userid):
        theuser = GamefaqUser.objects.get(id=userid)
        theuser.followers.remove(request.user)
        theuser.save()
        return HttpResponseRedirect(f"/user_profile_view/{userid}")


class FavoriteView(LoginRequiredMixin, TemplateView):
    def get(self, request, gameid):
        theuser = request.user
        game = Game.objects.get(id=gameid)
        theuser.favorited_games.add(game)
        theuser.save()
        return HttpResponseRedirect(f"/game/{gameid}/")


class UnFavoriteView(LoginRequiredMixin, TemplateView):
    def get(self, request, gameid):
        theuser = request.user
        game = Game.objects.get(id=gameid)
        theuser.favorited_games.remove(game)
        theuser.save()
        return HttpResponseRedirect(f"/game/{gameid}")


class CommentView(LoginRequiredMixin, TemplateView):
    def get(self, request, userid):
        f = CommentForm()
        return render(request, 'form.html', {"f": f})

    def post(self, request, userid):
        if request.method == "POST":
            g = GamefaqUser.objects.get(id=userid)
            form = CommentForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                User_Comments.objects.create(
                    body=data.get('body'),
                    touser=g,
                    author=request.user
                )

                return HttpResponseRedirect(f"/user_profile_view/{userid}")


class ConsoleFavView(LoginRequiredMixin, TemplateView):
    def get(self, request, consoleid):
        theuser = request.user
        console = Console.objects.get(id=consoleid)
        theuser.preferred_systems.add(console)
        theuser.save()
        return HttpResponseRedirect(f"/console/{consoleid}/")


class ConsoleUnfavView(LoginRequiredMixin, TemplateView):
    def get(self, request, consoleid):
        theuser = request.user
        console = Console.objects.get(id=consoleid)
        theuser.preferred_systems.remove(console)
        theuser.save()
        return HttpResponseRedirect(f"/console/{consoleid}")


class edit_user_comment_view(LoginRequiredMixin, TemplateView):
    def get(self, request, commentid):
        comment = User_Comments.objects.get(id=commentid)
        if request.user.id == comment.author.id:
            data = {
                "body": comment.body
            }
            f = CommentForm(initial=data)
            return render(request, "form.html", {"f": f})
        else:
            return HttpResponseRedirect(reverse('home'))

    def post(self, request, commentid):
        comment = User_Comments.objects.get(id=commentid)
        userid = comment.touser.id
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                comment.body = data["body"]
                comment.save()
                return HttpResponseRedirect(f"/user_profile_view/{userid}/")


class DeleteComment(DeleteView):
    model = User_Comments
    template_name = "delete.html"
    success_url = "/"

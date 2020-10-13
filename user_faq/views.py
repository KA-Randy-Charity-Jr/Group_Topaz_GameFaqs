from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from user_faq.forms import GamefaqUserForm
from authentication.views import login_view
from user_faq.models import GamefaqUser
from user_faq.forms import SignupForm

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
                    preferred_systems=data.get("preferred_systems"),
                    username=data.get("username"),
                    password=data.get("password"),
                )
                login(request, new_user)
                return HttpResponseRedirect(reverse('home'))

def user_profile_view(request, user_id):
    html = 'user_profile.html'
    user_detail = GamefaqUser.objects.filter(id=user_id).first()
    return render(request, html, {'profile':user_detail})


class edit_user_profile_view(TemplateView):
    def get(self, request, user_id):
        faq_user = GamefaqUser.objects.get(id=user_id)
        data = {
            "displayname": faq_user.displayname,
            "bio": faq_user.bio,
            "preferred_systems": faq_user.preferred_systems,
            "email": faq_user.email
        }
        form = GamefaqUserForm(initial=data)
        return render(request, "basic.html", {"form": form})

    def post(self, request, user_id):
        faq_user = GamefaqUser.objects.get(id=user_id)
        if request.method == "POST":
            form = GamefaqUserForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                faq_user.displayname = data["displayname"]
                faq_user.bio = data["bio"]
                faq_user.preferred_systems = data["preferred_systems"]
                faq_user.email = data["email"]
                faq_user.save()
                return HttpResponseRedirect(reverse('user_profile', args=[faq_user.id]))                
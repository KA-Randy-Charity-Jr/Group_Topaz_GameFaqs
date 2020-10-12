from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

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
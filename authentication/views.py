from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, HttpResponseRedirect, reverse
from authentication.forms import LoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get(
                'username'), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse ("home")))
            else:
                return HttpResponseRedirect()
    form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))       
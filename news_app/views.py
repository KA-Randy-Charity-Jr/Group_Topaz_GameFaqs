from django.shortcuts import render
from django.views.generic import TemplateView
from news_app.forms import NewNewspost
from news_app.models import Newspost
from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
# Create your views here.

class Newspostform(TemplateView):
    def get(self, request):
        f = NewNewspost()
        return render(request,"form.html",{"f":f})
    def post(self, request):
        if request.method == "POST":
            form = NewNewspost(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                Newspost.objects.create(
                    title=data.get('title'),
                    body=data.get('body'),
                    author=request.user,
                    game=data.get('game')
                )
                
                return HttpResponseRedirect(reverse('home'))

def NewpostView(request, newsid):
    post = Newspost.objects.get(id=newsid)
    return render(request,"newspost.html",{"post":post})                
        
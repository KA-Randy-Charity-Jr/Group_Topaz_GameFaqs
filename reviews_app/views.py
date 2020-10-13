from django.shortcuts import render
from reviews_app.models import Review
from gamefaq_app.models import GameFaq
from django.views.generic import TemplateView
from reviews_app.forms import ReviewForm
from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse


# Create your views here.
def ReviewsView(request, faqid):
    reviews= Review.objects.filter(gamefaq=faqid)
    return render(request, "reviews.html", {"reviews": reviews})
    

class CreateReview(TemplateView):
    def get(self, request,faqid):
        f = ReviewForm()
        return render(request,"form.html",{"f":f})
    def post(self, request,faqid):
        reccomend=False
        if request.method == "POST":
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                if data.get('isreccomend') == 'YES':
                    reccomend = True
                Review.objects.create(
                    body=data.get('body'),
                    author=request.user,
                    gamefaq=GameFaq.objects.get(id=faqid),
                    isreccomend=reccomend
                )
                
                return HttpResponseRedirect(reverse('home'))
from django.shortcuts import render
from reviews_app.models import Review
from gamefaq_app.models import GameFaq
from django.views.generic import TemplateView
from reviews_app.forms import ReviewForm
from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView


# Create your views here.
def ReviewsView(request, faqid):
    reviews = Review.objects.filter(gamefaq=faqid).order_by("-id")
    faq = GameFaq.objects.get(id=faqid)

    return render(request, "reviews.html", {"reviews": reviews, 'faq': faq})


class CreateReview(LoginRequiredMixin, TemplateView):
    def get(self, request, faqid):
        f = ReviewForm()
        return render(request, "revform.html", {"f": f})

    def post(self, request, faqid):
        thefaq = GameFaq.objects.get(id=faqid)
        reccomend = False
        if request.method == "POST":
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                if data.get('isreccomend') == 'YES':
                    reccomend = True
                    thefaq.upvotes += 1
                else:
                    thefaq.downvotes -= 1
                thefaq.save()
                Review.objects.create(
                    body=data.get('body'),
                    author=request.user,
                    gamefaq=GameFaq.objects.get(id=faqid),
                    isreccomend=reccomend
                )

                return HttpResponseRedirect('')


class Edit_ReviewView(LoginRequiredMixin, TemplateView):
    def get(self, request, reviewid):
        reccomend = ""
        review = Review.objects.get(id=reviewid)
        if request.user.id == review.author.id:
            if review.isreccomend == True:
                reccomend = "YES"
            else:
                reccomend: "NO"
            data = {
                "body": review.body,
                "isreccomend": reccomend
            }
            f = ReviewForm(initial=data)
            return render(request, "revform.html", {"f": f})
        else:
            return HttpResponseRedirect('')

    def post(self, request, reviewid):
        isreccomend = False
        review = Review.objects.get(id=reviewid)

        if request.method == "POST":
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                if data.get('isreccomend') == "YES":
                    isreccomend = True

                review.isreccomend = isreccomend
                review.body = data["body"]
                review.save()
                return HttpResponseRedirect(f"/{review.gamefaq.id}/reviews/")


class DeleteReview(DeleteView):
    model = Review
    template_name = "delete.html"
    success_url = "/"

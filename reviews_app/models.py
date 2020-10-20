from django.db import models
from gamefaq_app.models import GameFaq
from user_faq.models import GamefaqUser

# Create your models here.


class Review(models.Model):
    body = models.TextField()
    isreccomend = models.BooleanField()
    gamefaq = models.ForeignKey(
        GameFaq, on_delete=models.CASCADE, related_name="reviewgamefaq")
    author = models.ForeignKey(
        GamefaqUser, on_delete=models.CASCADE, related_name="review_author")

    def __str__(self):
        return f"{self.author} review{self.id}"

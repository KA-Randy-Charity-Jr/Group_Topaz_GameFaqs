from django.db import models
from game_app.models import Game
from user_faq.models import GamefaqUser

# Create your models here.
class Newspost(models.Model):
    title = models.CharField(max_length=150)
    body= models.TextField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="thegame")
    author = models.OneToOneField(GamefaqUser, on_delete=models.CASCADE,related_name="news_author")
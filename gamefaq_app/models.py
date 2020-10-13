from django.db import models
from user_faq.models import GamefaqUser
from game_app.models import Game
from console_app.models import Console
from django.utils import timezone

# Create your models here.
class GameFaq(models.Model):
    difficulties= [('EASY','EASY'),('INTERMEDIATE','INTERMEDIATE'),('HARD','HARD')]
    title = models.CharField(max_length=300)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="faq_game",default=True)
    body = models.TextField()
    difficulty = models.CharField(max_length=85, choices=difficulties)
    consoles = models.ManyToManyField(Console, symmetrical=False, blank=True, related_name="console_gamefaq")
    author = models.ForeignKey(GamefaqUser, on_delete=models.CASCADE, related_name="gamefaq_author")
    postdate = models.DateTimeField(default=timezone.now)   
    def __str__(self):
        return self.title
    
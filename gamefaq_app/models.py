from django.db import models
from user_faq.models import GamefaqUser
from game_app.models import Game
from console_app.models import Console
from django.utils import timezone

# Create your models here.
class GameFaq(models.Model):
    difficulties= [('EASY','EASY'),('INTERMEDIATE','INTERMEDIATE'),('HARD','HARD')]
    title = models.CharField(max_length=300)
    game = models.ForeignKey(Game,  on_delete=models.CASCADE, related_name="faq_game")
    body = models.TextField()
    difficulty = models.CharField(max_length=85, choices=difficulties)
    consoles = models.ForeignKey(Console,on_delete=models.CASCADE, blank=True, related_name="console_gamefaq", null=True)
    author = models.ForeignKey(GamefaqUser, on_delete=models.CASCADE, related_name="gamefaq_author")
    postdate = models.DateTimeField(default=timezone.now),
    ptype = models.CharField(max_length=25, choices=[('CHEATCODES', 'CHEATCODES'), ('GAMEFAQ', 'GAMEFAQ')], default='GAMEFAQ')
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    
    def added(self):
        return self.upvotes + self.downvotes
    def __str__(self):
        return self.title
    
from django.contrib.auth.models import AbstractUser
from django.db import models
from game_app.models import Game
from console_app.models import Console
from django.utils import timezone

# Create your models here.


class GamefaqUser(AbstractUser):
    displayname = models.CharField(max_length=80)
    bio = models.TextField(blank=True, null=True)
    preferred_systems = models.ManyToManyField(
        Console, symmetrical=False, blank=True)
    followers = models.ManyToManyField("self", symmetrical=False, blank=True)
    favorited_games = models.ManyToManyField(
        Game, symmetrical=False, related_name="user_fav")

    def __str__(self):
        return self.username


class User_Comments(models.Model):
    body = models.TextField()
    touser = models.ForeignKey(
        GamefaqUser, on_delete=models.CASCADE, related_name="taggeduser")
    author = models.ForeignKey(
        GamefaqUser, on_delete=models.CASCADE, related_name="comment_author")
    post_date = models.DateField(default=timezone.now)

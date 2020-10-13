from django.db import models
from console_app.models import Console


# Create your models here.
class Game(models.Model):
    genres=[('ACTION','ACTION'),('RPG','RPG'),('SHOOTER','SHOOTER'),('HORROR',"HORROR"),]
    title = models.CharField(max_length=100)
    genre = models.TextField(
        max_length=40,
        choices= genres
    )
   
    consoles = models.ManyToManyField(Console, symmetrical=False, blank=True, related_name="console_game")
    date_realesed = models.DateField()
    image = models.ImageField(upload_to="gallery")
    def __str__(self):
        return self.title 
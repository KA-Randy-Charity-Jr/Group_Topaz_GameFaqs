from django.db import models


class Gamefaq(models.Model):
    body = models.CharField(max_length=280)
    game = models.ForeignKey("Game", blank=True, on_delete=models.CASCADE, related_name="game")

    def __str__(self):
        return self.body
        
  
class Game(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    gamefaqs = models.ManyToManyField(Gamefaq, blank=True, related_name="faqs")
    date_realesed = models.DateField()
    image = models.ImageField(upload_to="gallery")
    

    def __str__(self):
        return self.name

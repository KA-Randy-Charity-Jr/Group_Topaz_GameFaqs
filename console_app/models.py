from django.db import models

# Create your models here.
class Console(models.Model):
    brands= [("XBOX","XBOX"),("PC","PC"),("PLAYSTATION","PLAYSTATION"),("NINTENDO","NINTENDO")]
    brand = models.CharField(max_length=25, choices=brands)
    name = models.CharField(max_length=45)
    


    def __str__(self):
        return self.name
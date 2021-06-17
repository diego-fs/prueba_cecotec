#Third party imports
from django.db import models
##Module imports
from random import randint

class Article(models.Model):
    code = models.CharField(unique=True, max_length=255, editable=False)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    size = models.FloatField()
    colour = models.CharField(max_length=25)
    
    def save(self, *args, **kwargs):
        ini = self.name[:1].upper()
        self.code = f"{ini}_{randint(10000, 1000000)}"
        
        super(Article, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name
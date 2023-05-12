from django.db import models

class products(models.Model):
    def __str__(self) -> str:
        return self.name
    
    name = models.CharField(max_length=50)
    price= models.FloatField()


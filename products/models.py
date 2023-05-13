from django.db import models

class products(models.Model):
    def __str__(self) -> str:
        return f"{self.name} : {self.price}"
    
    name = models.CharField(max_length=50)
    price= models.FloatField()


from django.db import models

class user(models.Model):
    def __str__(self) -> str:
        return self.firstName
    
    firstName = models.CharField(max_length=50)
    lastName  = models.CharField(max_length=50)
    phone     = models.IntegerField(null=True)
    create_at = models.DateField(null=True)


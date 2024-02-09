from django.db import models
from django.contrib.auth.models import User

class Guest(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    middle_name =  models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15)
    
    def __str__(self) -> str:
        return f'{self.first_name}-{self.last_name}'
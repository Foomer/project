from django.db import models


class Guest(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name =  models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15)
    
    def __str__(self) -> str:
        return f'{self.first_name}-{self.last_name}'
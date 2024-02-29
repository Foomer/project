from django.db import models
from hotels.models.folio import Folio
from django.contrib.auth.models import User

class FolioPosting(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    folio = models.ForeignKey(Folio,on_delete=models.CASCADE)
    note = models.CharField(max_length=50,blank=True)
    amount = models.FloatField()
    department = models.CharField(max_length=20)
    revenue = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return f'{self.note}-{self.amount}'
    
    
        
    
from django.db import models

from hotels.models.folio import Folio


class FolioPosting(models.Model):
    folio = models.ForeignKey(Folio,on_delete=models.CASCADE)
    note = models.CharField(max_length=50)
    amount = models.FloatField()
    department = models.CharField(max_length=20)
    revenue = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return f'{self.note}-{self.amount}'
    
        
    
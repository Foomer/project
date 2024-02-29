from django.db import models
from hotels.models import Folio
from django.contrib.auth.models import User

class Payment(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    folio = models.ForeignKey(Folio,on_delete=models.CASCADE,related_name='payments')
    type = models.CharField(max_length=10)
    amount = models.FloatField()
    note = models.TextField(blank=True)
    

    
    def __str__(self) -> str:
        return f'#{self.type} {self.amount}'
    

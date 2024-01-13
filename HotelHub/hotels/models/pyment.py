from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from hotels.models import Folio


class Payment(models.Model):
    folio = models.ForeignKey(Folio,on_delete=models.CASCADE,related_name='payments')
    type = models.CharField(max_length=10)
    amount = models.FloatField()
    note = models.TextField(blank=True)
    

    
    def __str__(self) -> str:
        return f'#{self.type} {self.amount}'
    
@receiver(post_save, sender=Payment)
def add_payment_to_folio(sender, instance, **kwargs):
    instance.folio.payment.add(instance)
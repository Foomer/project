from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from hotels.models.folio import Folio


class FolioPosting(models.Model):
    folio = models.ForeignKey(Folio,on_delete=models.CASCADE)
    note = models.CharField(max_length=50,blank=True)
    amount = models.FloatField()
    department = models.CharField(max_length=20)
    revenue = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return f'{self.note}-{self.amount}'
    
@receiver(post_save, sender=FolioPosting)
def add_folio_posting_to_folio(sender, instance, **kwargs):
    instance.folio.folio_postings.add(instance)
    
        
    
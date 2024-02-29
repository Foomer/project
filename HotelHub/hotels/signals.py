from models import Payment,FolioPosting

from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=Payment)
def add_payment_to_folio(sender, instance, **kwargs):
    instance.folio.payment.add(instance)
    
    
@receiver(post_save, sender=FolioPosting)
def add_folio_posting_to_folio(sender, instance, **kwargs):
    instance.folio.folio_postings.add(instance)
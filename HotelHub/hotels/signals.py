from hotels.models import Payment,FolioPosting,Guest,Folio

from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=Guest)
def create_folio(sender,instance,created,**kwargs):
    if created:
        Folio.objects.create(user=instance.user, guest=instance)

@receiver(post_save, sender=Payment)
def add_payment_to_folio(sender, instance, **kwargs):
    instance.folio.payment.add(instance)
    
    
@receiver(post_save, sender=FolioPosting)
def add_folio_posting_to_folio(sender, instance, **kwargs):
    instance.folio.folio_postings.add(instance)
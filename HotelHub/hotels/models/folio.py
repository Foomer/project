from django.db import models


from hotels.models.guest import Guest
from django.contrib.auth.models import User

class Folio(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest,on_delete=models.CASCADE)
    folio_postings = models.ManyToManyField('hotels.FolioPosting', related_name='folio_postings',blank=True)
    payment = models.ManyToManyField('hotels.Payment',blank=True, related_name='folios')
    
    
    @property
    def total_price(self):
        total_price = 0
        payment_amount=0
        for posting in self.folio_postings.all():
            total_price += posting.amount
        for payment in self.payment.all():
            payment_amount += payment.amount
        return total_price - payment_amount
    
    def __str__(self):
        return f'Folio for {self.guest.first_name} {self.total_price}'
    
    
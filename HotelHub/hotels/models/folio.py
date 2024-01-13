from django.db import models


from hotels.models.guest import Guest

class Folio(models.Model):
    guest = models.ForeignKey(Guest,on_delete=models.CASCADE)
    folio_postings = models.ManyToManyField('hotels.FolioPosting', related_name='folio_postings',blank=True)
    
    def __str__(self):
        return f'Folio for {self.guest.first_name}'
    
    
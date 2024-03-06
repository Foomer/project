from django.apps import AppConfig


class HotelsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hotels'
    
    def ready(self) -> None:
        from hotels.signals import create_folio
        from hotels.signals import add_payment_to_folio
        from hotels.signals import add_folio_posting_to_folio


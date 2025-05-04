from django.apps import AppConfig

class EcommerceProjectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ecommerce_project'

    def ready(self):
        from .mongodb import connect_to_mongodb
        connect_to_mongodb() 
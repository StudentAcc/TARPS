from django.apps import AppConfig
from .recommender import start

class StocksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stocks'

    def ready(self):
        start()

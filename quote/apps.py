from django.apps import AppConfig


class QuoteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quote'

def ready(self):
    import quote.signals  # Замените "your_app" на название вашего приложения

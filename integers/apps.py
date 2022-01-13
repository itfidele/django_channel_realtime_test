from django.apps import AppConfig


class IntegersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'integers'

    def ready(self):
        from . import signals

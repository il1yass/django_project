from django.apps import AppConfig


class BangConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'baimed'
    def ready(self):
        import baimed.signals

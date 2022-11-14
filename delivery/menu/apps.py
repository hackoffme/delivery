from django.apps import AppConfig


class MyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'menu'
    verbose_name = 'Меню'
    
    def ready(self) -> None:
        from . import signals

from django.apps import AppConfig


class BasesiteConfig(AppConfig):
    name = 'basesite'
    verbose_name = "Фильмы"


    def ready(self):
        import basesite.signal

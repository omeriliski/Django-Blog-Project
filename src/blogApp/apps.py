from django.apps import AppConfig


class BlogappConfig(AppConfig):
    name = 'blogApp'

    def ready(self):
        import blogApp.signals
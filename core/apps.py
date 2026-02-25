from django.apps import AppConfig
def ready(self):
    import core.signals

class CoreConfig(AppConfig):
    name = 'core'

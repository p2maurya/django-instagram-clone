from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        import os

        # keep your signals import if needed
        try:
            import core.signals
        except:
            pass

        if os.environ.get("RENDER") == "true":
            from django.contrib.auth import get_user_model
            User = get_user_model()

            if not User.objects.filter(username="admin").exists():
                User.objects.create_superuser(
                    "admin",
                    "admin@example.com",
                    "admin123"
                )
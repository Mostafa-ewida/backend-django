from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RoomsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = _("hackmaze.rooms")

    def ready(self):
        try:
            import hackmaze.rooms.signals  # noqa: F401
        except ImportError:
            pass

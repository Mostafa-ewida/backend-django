from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RoomsConfig(AppConfig):
    name = "hackmaze.rooms"
    verbose_name = _("Rooms")

    def ready(self):
        try:
            import hackmaze.rooms.signals  # noqa: F401
        except ImportError:
            pass

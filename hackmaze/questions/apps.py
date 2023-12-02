from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class QuestionsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "hackmaze.questions"


class UsersConfig(AppConfig):
    name = "hackmaze.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import hackmaze.questions.signals  # noqa: F401
        except ImportError:
            pass

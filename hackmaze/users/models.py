from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from hackmaze.users.managers import UserManager
from django.utils.translation import gettext as _
from django.db import models


from hackmaze.custom_models import AbstractModel


class User(AbstractUser):
    """
    Default custom user model for hackmake backend.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    email = EmailField(_("email address"), unique=True)
    username = None  # type: ignore

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"pk": self.id})


class UserProfile(AbstractModel):
    bio = models.TextField(null=True, blank=True)
    blog_url = models.URLField(max_length=255, null=True, blank=True)
    exp_level = models.IntegerField()
    github_url = models.URLField(max_length=255, null=True, blank=True)
    job = models.CharField(max_length=255)
    linkedin_url = models.URLField(max_length=255, null=True, blank=True)
    rank = models.IntegerField(_("User rank accross the platform"))
    twitter_url = models.URLField(max_length=255, null=True, blank=True)

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    """
    country: django country filed
    TODO: use https://pypi.org/project/django-countries/ instead
    XXX: use ip_forword_x to get it's country
    website_admin (is_staff)

    """

    @property
    def full_name(self):
        return self.first_name + self.last_name

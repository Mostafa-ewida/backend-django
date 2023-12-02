from django.db import models
from taggit.managers import TaggableManager

from hackmaze.users.models import UserProfile as Author


# Create your models here.
class Room(models.Model):
    DIFFICULTY_CHOICES = [
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard"),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    visibility = models.BooleanField(default=True)  # True for public, False for private
    recommended_video = models.URLField(blank=True, null=True)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default="medium")
    tags = TaggableManager()

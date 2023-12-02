from django.db import models
from taggit.managers import TaggableManager

from hackmaze.users.models import UserProfile as Author

from .constants import DIFFICULTY_CHOICES, MACHINE, PUBLIC, TYPE_CHOICES, VISIBILITY_CHOICES


# Create your models here.
class Room(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    room_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default=MACHINE)
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, default=PUBLIC)
    recommended_video = models.URLField(blank=True, null=True)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default="medium")
    tags = TaggableManager()

    def __str__(self):
        return self.title


class Collection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    rooms = models.ManyToManyField(Room)

    def __str__(self):
        return self.title


class Module(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    level = models.IntegerField()
    is_active = models.BooleanField(default=False)
    collections = models.ManyToManyField(Collection)

from django.db import models

from hackmaze.rooms.models import Room


class Section(models.Model):
    """
    Model representing a section that can contain multiple questions.
    """

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="sections")
    order = models.PositiveIntegerField()  # To determine the order of sections in a room

    def __str__(self):
        return f"{self.title} - {self.room.title}"


class Question(models.Model):
    """
    Model representing a question within a section.
    """

    text = models.TextField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="questions")
    order = models.PositiveIntegerField()  # To determine the order of questions in a section

    def __str__(self):
        return f"Question {self.order} - {self.section.title}"

from django.db import models
from .enum import StatusChoices
from user.models import CustomUser


class Tag(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True
    )
    color = models.CharField(
        max_length=20,
    )

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(
        max_length=255
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.TODO
    )
    assignee = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True
    )

    def __str__(self):
        return self.title

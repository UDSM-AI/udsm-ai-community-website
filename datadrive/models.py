from django.db import models
from django.db.models import Count

class MovementCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.name


class Movement(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(MovementCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MovementEntry(models.Model):
    movement = models.ForeignKey(Movement, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='audio/')
    notes = models.TextField()

    def __str__(self):
        return self.movement.name

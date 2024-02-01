from django.db import models



class MovementCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image_url = models.URLField()


class Movement(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(MovementCategory, on_delete=models.CASCADE)


class MovementEntry(models.Model):
    movement = models.ForeignKey(Movement, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='audio/')
    notes = models.TextField()

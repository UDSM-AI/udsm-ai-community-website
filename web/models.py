from django.db import models

class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Highlight(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='event_images/')
    description = models.TextField()
    event_date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.title


class StudentReview(models.Model):
    name = models.CharField(max_length=255)
    classification = models.CharField(max_length=255)
    comments = models.TextField()

    def __str__(self):
        return self.name


class TeamLead(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.FileField(upload_to="leads/")
    social_links = models.TextField()

    def __str__(self):
        return self.name


class ContactInfo(models.Model):
    headquarter = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    copyright = models.CharField(max_length=255)
    designer = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    careers_link = models.URLField()
    investor_link = models.URLField()
    terms_conditions_link = models.URLField()

    def __str__(self):
        return f"{self.headquarter} - {self.university}"
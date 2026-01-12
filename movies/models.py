from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    poster = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    release_date = models.DateField()

    genres = models.ManyToManyField(Genre)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.title
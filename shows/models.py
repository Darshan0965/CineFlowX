from django.db import models
from movies.models import Movie


class Theatre(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=200, default="Chennai")

    def __str__(self):
        return self.name


class Screen(models.Model):
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rows = models.IntegerField(default=10)
    cols = models.IntegerField(default=16)

    def __str__(self):
        return f"{self.theatre.name} - {self.name}"


class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    show_time = models.TimeField()

    def __str__(self):
        return f"{self.movie.title} @ {self.show_time}"


class Seat(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    row = models.CharField(max_length=1)
    number = models.IntegerField()
    price = models.IntegerField(default=150)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.row}{self.number}"
from django.core.management.base import BaseCommand
from movies.models import Movie, Genre, Language
from shows.models import Theatre, Screen, Show, Seat
from datetime import time, date
import string


class Command(BaseCommand):
    help = "Seed complete BookMyShow data"

    def handle(self, *args, **kwargs):

        Seat.objects.all().delete()
        Show.objects.all().delete()
        Screen.objects.all().delete()
        Theatre.objects.all().delete()
        Movie.objects.all().delete()
        Genre.objects.all().delete()
        Language.objects.all().delete()

        # Genres & Languages
        action = Genre.objects.create(name="Action")
        scifi = Genre.objects.create(name="Sci-Fi")
        drama = Genre.objects.create(name="Drama")

        english = Language.objects.create(name="English")
        tamil = Language.objects.create(name="Tamil")

        movies_data = [
            ("Avatar 3", "movies/posters/avatar.jpg", scifi, english),
            ("Batman 2", "movies/posters/batman.jpg", action, english),
            ("Avengers: The Secret War", "movies/posters/avengers.jpg", action, english),
            ("Fast and Furious 2", "movies/posters/fast.jpg", action, english),
            ("Devara 2", "movies/posters/devara.jpg", drama, tamil),
            ("Kanguva 2", "movies/posters/kanguva.jpg", action, tamil),
            ("Pushpa 3", "movies/posters/pushpa.jpg", action, tamil),
            ("Vaa Vaathiyaar", "movies/posters/vaavaathiyaar.jpg", drama, tamil),
        ]

        movies = []
        for title, poster, genre, lang in movies_data:
            movie = Movie.objects.create(
                title=title,
                poster=poster,
                description=title,
                release_date=date(2025, 12, 25)
            )
            movie.genres.add(genre)
            movie.languages.add(lang)
            movies.append(movie)

        theatres = [
            Theatre.objects.create(name="PVR Cinemas"),
            Theatre.objects.create(name="SPI Palazzo"),
        ]

        screens = []
        for theatre in theatres:
            screens.append(Screen.objects.create(
                theatre=theatre,
                name="Screen 1",
                rows=9,
                cols=16
            ))

        times = [time(9,30), time(12,45), time(16,0), time(19,30), time(22,15)]

        for movie in movies:
            for screen in screens:
                for t in times:
                    show = Show.objects.create(
                        movie=movie,
                        theatre=screen.theatre,
                        screen=screen,
                        show_time=t
                    )

                    for r in range(screen.rows):
                        row_letter = string.ascii_uppercase[r]
                        for c in range(1, screen.cols + 1):
                            Seat.objects.create(
                                show=show,
                                row=row_letter,
                                number=c,
                                price=150
                            )

        self.stdout.write(self.style.SUCCESS("✅ FULL BookMyShow data seeded"))
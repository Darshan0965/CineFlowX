from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Seat, Booking
from movies.models import Movie


@login_required
def select_seat(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    # Create seats only once
    if not Seat.objects.filter(movie=movie).exists():
        for i in range(1, 11):
            Seat.objects.create(movie=movie, seat_number=f"A{i}")

    seats = Seat.objects.filter(movie=movie)

    return render(request, 'bookings/select_seat.html', {
        'movie': movie,
        'seats': seats
    })


@login_required
def book_seat(request, seat_id):
    seat = get_object_or_404(Seat, id=seat_id)

    if seat.is_booked:
        return redirect('select_seat', movie_id=seat.movie.id)

    seat.is_booked = True
    seat.save()

    Booking.objects.create(
        user=request.user,
        movie=seat.movie,
        seat=seat
    )

    return render(request, 'bookings/success.html', {
        'seat': seat
    })
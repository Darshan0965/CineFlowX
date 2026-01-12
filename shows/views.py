from django.shortcuts import render, get_object_or_404
from .models import Show, Seat


def theatre_list(request, movie_id):
    shows = Show.objects.filter(movie_id=movie_id).select_related('theatre')

    theatre_shows = {}
    for show in shows:
        theatre_shows.setdefault(show.theatre, []).append(show)

    return render(request, 'shows/theatre_list.html', {
        'theatre_shows': theatre_shows
    })


def seat_layout(request, show_id):
    show = get_object_or_404(Show, id=show_id)
    seats = Seat.objects.filter(show=show).order_by('row', 'number')

    return render(request, 'shows/seat_layout.html', {
        'show': show,
        'seats': seats
    })
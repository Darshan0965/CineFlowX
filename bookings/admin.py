from django.contrib import admin
from .models import Seat, Booking

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('seat_number', 'movie', 'is_booked')
    list_filter = ('movie', 'is_booked')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'seat', 'booked_at')
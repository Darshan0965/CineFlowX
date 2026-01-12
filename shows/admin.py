from django.contrib import admin
from .models import Theatre, Screen, Show


@admin.register(Theatre)
class TheatreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')


@admin.register(Screen)
class ScreenAdmin(admin.ModelAdmin):
    list_display = ('name', 'theatre')


@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ('movie', 'theatre', 'screen', 'show_time')
    list_filter = ('theatre', 'movie')
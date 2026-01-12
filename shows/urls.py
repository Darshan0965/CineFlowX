from django.urls import path
from . import views

app_name = 'shows'

urlpatterns = [
    path('theatres/<int:movie_id>/', views.theatre_list, name='theatre_list'),
    path('seat-layout/<int:show_id>/', views.seat_layout, name='seat_layout'),
]
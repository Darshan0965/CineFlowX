from django.urls import path
from . import views

urlpatterns = [
    path('seats/<int:movie_id>/', views.select_seat, name='select_seat'),
    path('book/<int:seat_id>/', views.book_seat, name='book_seat'),
]
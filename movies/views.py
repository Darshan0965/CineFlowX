from django.shortcuts import render
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all()

    selected_genre = request.GET.get('genre')
    selected_language = request.GET.get('language')

    # ✅ FILTER BY TEXT (NOT ID)
    if selected_genre:
        movies = movies.filter(genres__icontains=selected_genre)

    if selected_language:
        movies = movies.filter(languages__icontains=selected_language)

    # ✅ DISTINCT VALUES FOR DROPDOWNS
    genres = Movie.objects.values_list('genres', flat=True).distinct()
    languages = Movie.objects.values_list('languages', flat=True).distinct()

    context = {
        'movies': movies,
        'genres': genres,
        'languages': languages,
        'selected_genre': selected_genre,
        'selected_language': selected_language,
    }

    return render(request, 'movies/movie_list.html', context)
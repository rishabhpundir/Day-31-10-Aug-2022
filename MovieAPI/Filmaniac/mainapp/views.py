from mainapp.models import Movie
from django.http import JsonResponse

# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    data = {'movies': list(movies.values())}
    return JsonResponse(data)

def movie_details(request, movie_id):
    details = Movie.objects.get(pk=movie_id)
    data = {
        'name': details.name,
        'genre': details.genre,
        'release': details.release,
        'description': details.description,
        'active': details.active
    }
    return JsonResponse(data)

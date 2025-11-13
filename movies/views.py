
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movies/add_movie.html', {'form': form})


def horror_genre(request):
    return render(request, 'movies/horror_genre.html')

def cinema(request):
    return render(request, 'movies/cinema.html',)




from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer
from rest_framework import viewsets, filters

class MovieList(APIView):
    def get(self, request):
        movies = Movie.objects.all()            # prendi tutti i film
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

from rest_framework import viewsets

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()       # tutti i film
    serializer_class = MovieSerializer   # come trasformarli in JSON
    filter_backends = [filters.SearchFilter]   # abilita la ricerca
    search_fields = ['title']    

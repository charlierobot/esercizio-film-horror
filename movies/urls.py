from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('add/', views.add_movie, name='add_movie'),  # addddddd
    path('horror-genre/', views.horror_genre, name='horror_genre'),
    path('cinema/', views.cinema, name='cinema'), #page con cards
]


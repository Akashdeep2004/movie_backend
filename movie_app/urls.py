from django.urls import path
from .views import movie_list, movie_details, movie_request

api_key = "9039591815ashish_verma"

urlpatterns = [
    path('9039591815ashish_verma/movies/', movie_list, name='movie-list'),
    path('9039591815ashish_verma/movies/<int:pk>/', movie_details, name='movie_details'),
    path('9039591815ashish_verma/request/movie/', movie_request, name='request_movie'),
    
]

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie, Note
from .serializers import MovieSerializer, NoteSerializer

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_details(request, pk):
    movie = Movie.objects.get(id=pk)
    serializer = MovieSerializer(movie, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def movie_request(request):
    data = request.data
    name = data.get('name', '')
    message = data.get('request', '')

    note = Note.objects.create(
    name=name,
    message=message
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)
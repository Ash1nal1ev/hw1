from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app import serializers
from . import models
from rest_framework import status

@api_view(['GET'])
def director_list_view(request):
    director = models.Director.objects.all()
    data = serializers.DirectorSerializer(director, many=True).data
    return Response(data=data)

@api_view(["GET"])
def director_detail_view(request, id):
    director = models.Director.objects.get(id=id)
    data = serializers.DirectorSerializer(director).data
    return Response(data=data)

@api_view(["GET"])
def movie_list_view(request):
    movie = models.Movie.objects.all()
    data = serializers.MovieSerializer(movie, many=True).data
    return Response(data=data)

@api_view(["GET"])
def movie_detail_view(request, id):
    movie = models.Movie.objects.get(id=id)
    data = serializers.MovieSerializer(movie).data
    return Response(data=data)

@api_view(["GET"])
def review_list_view(request):
    review = models.Review.objects.all()
    data = serializers.ReviewSerializer(review, many=True).data
    return Response(data=data)

@api_view(["GET"])
def review_detail_view(request, id):
    review = models.Review.objects.get(id=id)
    data = serializers.ReviewSerializer(review).data
    return Response(data=data)

@api_view(["GET"])
def review_movie_list_view(request):
    movie = models.Movie.objects.all()
    data = serializers.ReviewMovieSerializer(movie, many=True).data
    return Response(data=data)
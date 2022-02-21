from importlib.metadata import requires
from os import stat
from turtle import title
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app import serializers
from . import models
from rest_framework import status

@api_view(['GET', 'POST'])
def director_list_view(request):
    if request.method == 'GET':
        director = models.Director.objects.all()
        data = serializers.DirectorSerializer(director, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        name = request.data.get('name')
        director = models.Director.objects.create(name=name)
        return Response(data=serializers.DirectorSerializer(director).data, status=status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
def director_detail_view(request, id):
    try:
        director = models.Director.objects.get(id=id)
    except models.Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Not Found'})
    if request.method == "GET":
        data = serializers.DirectorSerializer(director).data
        return Response(data=data)
    elif request.method == "PUT":
        director.name = request.data.get("name")
        director.save()
        return Response(serializers.DirectorSerializer(director).data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET", "POST"])
def movie_list_view(request):
    if request.method == "GET":
        movie = models.Movie.objects.all()
        data = serializers.MovieSerializer(movie, many=True).data
        return Response(data=data)
    elif request.method == "POST":
        title= request.data.get("title")
        description = request.data.get("description")
        duration = request.data.get("duration")
        director_id = request.data.get("director_id")
        movie = models.Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
        return Response(data=serializers.MovieSerializer(movie).data, status=status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
def movie_detail_view(request, id):
    try:
        movie = models.Movie.objects.get(id=id)
    except models.Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Not Found'})
    if request.method == "GET":
        data = serializers.MovieSerializer(movie).data
        return Response(data=data)
    elif request.method == "PUT":
        movie.title= request.data.get("title")
        movie.description = request.data.get("description")
        movie.duration = request.data.get("duration")
        movie.director_id = request.data.get("director_id")
        movie.save()
        return Response(serializers.MovieSerializer(movie).data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET", "POST"])
def review_list_view(request):
    if request.method == "GET":
        review = models.Review.objects.all()
        data = serializers.ReviewSerializer(review, many=True).data
        return Response(data=data)
    elif request.method == "POST":
        text = request.data.get("text")
        movie_id = request.data.get("movie_id")
        stars = request.data.get("stars")
        review = models.Review.objects.create(text=text, movie_id=movie_id, stars=stars)
        return Response(data=serializers.ReviewSerializer(review).data, status=status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
def review_detail_view(request, id):
    try:
        review = models.Review.objects.get(id=id)
    except models.Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Not Found'})
    if request.method == "GET":
        data = serializers.ReviewSerializer(review).data
        return Response(data=data)
    elif request.method == "PUT":
        review.text = request.data.get("text")
        review.movie_id = request.data.get("movie_id")
        review.stars = request.data.get("stars")
        review.save()
        return Response(serializers.ReviewSerializer(review).data)
    elif request.method == "DELETE":
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET"])
def review_movie_list_view(request):
    movie = models.Movie.objects.all()
    data = serializers.ReviewMovieSerializer(movie, many=True).data
    return Response(data=data)
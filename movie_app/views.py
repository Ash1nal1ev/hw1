from rest_framework.generics import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app import serializers
from . import models
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
import random
import smtplib


class DirectorListAPIView(ListCreateAPIView):
    serializer_class = serializers.DirectorSerializer
    queryset = models.Director.objects.filter().order_by("-id")

    def post(self, request):
        serializer = serializers.DirectorCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        director = models.Director.objects.create(**serializer.validated_data)
        return Response(data=serializers.DirectorSerializer(director).data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'POST'])
# def director_list_view(request):
#     if request.method == 'GET':
#         director = models.Director.objects.all()
#         data = serializers.DirectorSerializer(director, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializer = serializers.DirectorCreateUpdateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(data={"errors":serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
#         else:
#             name = request.data.get('name')
#             director = models.Director.objects.create(name=name)
#             return Response(data=serializers.DirectorSerializer(director).data, status=status.HTTP_201_CREATED)

class DirectorUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Director.objects.all()
    serializer_class = serializers.DirectorSerializer
    lookup_field = "id"


# @api_view(["GET", "PUT", "DELETE"])
# def director_detail_view(request, id):
#     try:
#         director = models.Director.objects.get(id=id)
#     except models.Director.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Not Found'})
#     if request.method == "GET":
#         data = serializers.DirectorSerializer(director).data
#         return Response(data=data)
#     elif request.method == "PUT":
#         serializer = serializers.DirectorCreateUpdateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(data={"errors":serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
#         else:
#             director.name = request.data.get("name")
#             director.save()
#             return Response(serializers.DirectorSerializer(director).data)
#     elif request.method == 'DELETE':
#         director.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class MovieListAPIView(ListCreateAPIView):
    serializer_class = serializers.MovieSerializer
    queryset = models.Movie.objects.filter().order_by("-id")

    def post(self, request):
        serializer = serializers.MovieCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        title = request.data.get("title")
        description = request.data.get("description")
        duration = request.data.get("duration")
        director_id = request.data.get("director_id")
        movie = models.Movie.objects.create(title=title, description=description,
                                            duration=duration, director_id=director_id)
        return Response(data=serializers.MovieSerializer(movie).data, status=status.HTTP_201_CREATED)


# @api_view(["GET", "POST"])
# def movie_list_view(request):
#     if request.method == "GET":
#         movie = models.Movie.objects.all()
#         data = serializers.MovieSerializer(movie, many=True).data
#         return Response(data=data)
#     elif request.method == "POST":
#         serializer = serializers.MovieCreateUpdateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(data={"errors":serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
#         else:
#             title= request.data.get("title")
#             description = request.data.get("description")
#             duration = request.data.get("duration")
#             director_id = request.data.get("director_id")
#             movie = models.Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
#             return Response(data=serializers.MovieSerializer(movie).data, status=status.HTTP_201_CREATED)

class MovieUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    lookup_field = "id"


# @api_view(["GET", "PUT", "DELETE"])
# def movie_detail_view(request, id):
#     try:
#         movie = models.Movie.objects.get(id=id)
#     except models.Movie.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Not Found'})
#     if request.method == "GET":
#         data = serializers.MovieSerializer(movie).data
#         return Response(data=data)
#     elif request.method == "PUT":
#         serializer = serializers.MovieCreateUpdateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(data={"errors":serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
#         else:
#             movie.title= request.data.get("title")
#             movie.description = request.data.get("description")
#             movie.duration = request.data.get("duration")
#             movie.director_id = request.data.get("director_id")
#             movie.save()
#             return Response(serializers.MovieSerializer(movie).data)
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class ReviewListAPIView(ListCreateAPIView):
    serializer_class = serializers.ReviewSerializer
    queryset = models.Review.objects.filter().order_by("-id")

    def post(self, request):
        serializer = serializers.ReviewCreateUpdateSerailizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = request.data.get("text")
        movie_id = request.data.get("movie_id")
        stars = request.data.get("stars")
        review = models.Review.objects.create(text=text, movie_id=movie_id, stars=stars)
        return Response(data=serializers.ReviewSerializer(review).data, status=status.HTTP_201_CREATED)


# @api_view(["GET", "POST"])
# def review_list_view(request):
#     if request.method == "GET":
#         review = models.Review.objects.all()
#         data = serializers.ReviewSerializer(review, many=True).data
#         return Response(data=data)
#     elif request.method == "POST":
#         serializer = serializers.ReviewCreateUpdateSerailizer(data=request.data)
#         if not serializer.is_valid():
#             return Response(data={"errors":serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
#         else:
#             text = request.data.get("text")
#             movie_id = request.data.get("movie_id")
#             stars = request.data.get("stars")
#             review = models.Review.objects.create(text=text, movie_id=movie_id, stars=stars)
#             return Response(data=serializers.ReviewSerializer(review).data, status=status.HTTP_201_CREATED)

class ReviewUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    lookup_field = "id"


# @api_view(["GET", "PUT", "DELETE"])
# def review_detail_view(request, id):
#     try:
#         review = models.Review.objects.get(id=id)
#     except models.Review.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Not Found'})
#     if request.method == "GET":
#         data = serializers.ReviewSerializer(review).data
#         return Response(data=data)
#     elif request.method == "PUT":
#         serializer = serializers.ReviewCreateUpdateSerailizer(data=request.data)
#         if not serializer.is_valid():
#             return Response(data={"errors":serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
#         else:
#             review.text = request.data.get("text")
#             review.movie_id = request.data.get("movie_id")
#             review.stars = request.data.get("stars")
#             review.save()
#             return Response(serializers.ReviewSerializer(review).data)
#     elif request.method == "DELETE":
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class ReviewMovieListAPIView(ListAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.ReviewMovieSerializer


# @api_view(["GET"])
# def review_movie_list_view(request):
#     movie = models.Movie.objects.all()
#     data = serializers.ReviewMovieSerializer(movie, many=True).data
#     return Response(data=data)

class RegisterAPIView(GenericAPIView):
    serializer_class = serializers.RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = request.data.get("username")
        password = request.data.get("password")
        User.objects.create_user(username=username, password=password)
        return Response(data={"message": "User created!"}, status=status.HTTP_201_CREATED)


class AuthorizateAPIView(GenericAPIView):
    serializer_class = serializers.AuthorizateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user:
            try:
                key_ = Token.objects.get(user=user)
            except Token.DoesNotExist:
                key_ = Token.objects.create(user=user)
            return Response(data={'key': key_.key})
        return Response(data={'error': 'User not found!'}, status=status.HTTP_404_NOT_FOUND)

# @api_view(['POST'])
# def authorization(request):
#     if request.method == 'POST':
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)
#         if user:
#             try:
#                 key_ = Token.objects.get(user=user)
#             except Token.DoesNotExist:
#                 key_ = Token.objects.create(user=user)
#             return Response(data={'key': key_.key})
#         return Response(data={'error':'User not found!'}, status=status.HTTP_404_NOT_FOUND)

# @api_view(['POST'])
# def registration(request):
#     if request.method == 'POST':
#         username = request.data.get('username')
#         password = request.data.get('password')
#         User.objects.create_user(username=username, password=password)
#         return Response(data={"message":"User created!"}, status=status.HTTP_201_CREATED)

# def verify_email(request):
#     code = random.randint(1000, 9999)
#     message = f"Your mail activation code: > [{code}] <"
#     sender = "testmailx22@.gmail.com"
#     password = "test12test"

#     server_ = smtplib.SMTP("smtp.gmail.com", 587)
#     server_.starttls()

#     try:
#         server_.login(sender, password)
#         server_.sendmail(sender, , message)
#     except Exception as _ex:
#         return f"{_ex}Пароль или логин указан неправильно!"




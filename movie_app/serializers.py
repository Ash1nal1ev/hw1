from rest_framework.exceptions import ValidationError
from rest_framework.serializers import SerializerMethodField
from rest_framework import serializers
from . import models

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = [
            "id",
            "name",
            "movies_count",
        ]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = [
            "id",
            "text",
            "movie",
            "stars",
        ]


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = [
            "id",
            "title",
            "description",
            "duration",
            "director",
        ]

class ReviewMovieSerializer(serializers.ModelSerializer):
    director = SerializerMethodField()

    review = SerializerMethodField()

    class Meta:
        model = models.Movie
        fields = [
            "id",
            "title",
            "description",
            "duration",
            "director",
            "review",
            'rating'
        ]
    def get_director(self, direc):
        try:
            return direc.director.name
        except:
            return "Пусто!"


    def get_review(self, rev):
        serializer = ReviewSerializer(rev.review.filter(text__isnull=False), many=True)
        return serializer.data

class DirectorCreateUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)

class ReviewCreateUpdateSerailizer(serializers.Serializer):
    text = serializers.CharField()
    movie_id = serializers.IntegerField()
    stars = serializers.IntegerField(min_value=1, max_value=5)

    def validate_movie_id(self, movie_id):
        if models.Movie.objects.filter(id=movie_id).count()==0:
            raise ValidationError(f'id {movie_id} does not exist')

class MovieCreateUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    duration = serializers.CharField(max_length=100)
    director_id = serializers.IntegerField()

    def validate_director_id(self, director_id):
        if models.Director.objects.filter(id=director_id).count()==0:
            raise ValidationError(f'id {director_id} does not exist')
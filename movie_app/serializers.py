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
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Director(models.Model):
    name = models.CharField(max_length=100)

    @property
    def movies_count(self):
        return self.director.all().count()

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField()
    duration = models.CharField( max_length=100, null=True, blank=True)
    director = models.ForeignKey(Director, on_delete=models.DO_NOTHING, related_name='director')

    @property
    def rating(self):
        reviews = Review.objects.filter(movie=self)
        stars = [ i.stars for i in reviews]
        return { 'средняя оценка': sum(stars)//len(stars)}

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='review')
    stars = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)

    def __str__(self):
        return f"Review: {self.movie.title}"
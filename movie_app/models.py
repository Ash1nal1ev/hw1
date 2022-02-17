from django.db import models

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
    duration = models.TimeField()
    director = models.ForeignKey(Director, on_delete=models.DO_NOTHING, related_name='director')

    @property
    def rating(self):
        reviews = Review.objects.filter(movie=self)
        stars = [ i.stars for i in reviews]
        return { 'средняя оценка': sum(stars)//len(stars)}

    def __str__(self):
        return self.title

class Review(models.Model):
    STARS = (
        (1,'Bad'),
        (2,'Nice'),
        (3,'Good'),
        (4,'Fine'),
        (5,'Amazing'),
    )
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='review')
    stars = models.PositiveIntegerField(max_length=5, choices=STARS,null=True)

    def __str__(self):
        return f"Review: {self.movie.title}"
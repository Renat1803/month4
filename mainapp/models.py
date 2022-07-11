from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)
    title = models.TextField(max_length=1000)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='movies', null=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.text
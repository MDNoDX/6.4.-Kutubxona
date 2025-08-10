from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=75, unique=True)

    def __str__(self):
        return f"{self.name}"
    
class Book(models.Model):
    title = models.CharField(max_length=75)
    author = models.CharField(max_length=75)
    description = models.TextField(null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
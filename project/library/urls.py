from django.urls import path
from .views import welcome, genre, book

urlpatterns = [
    path('', welcome, name='welcome'),
    path('genres/', genre, name='genres'),
    path('books/', book, name='books')
]
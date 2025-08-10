from django.shortcuts import render
from django.http import HttpRequest
from .models import Genre, Book

# Create your views here.

def welcome(request: HttpRequest):
    books = Book.objects.all()
    genres = Genre.objects.all()
    context = {
        "books": books,
        "genres": genres,
    }
    return render(request, 'book/welcome.html', context=context)

def genre(request: HttpRequest):
    genres = Genre.objects.all()
    context = {
        "genres": genres,
    }
    return render(request, 'book/genre.html', context=context)

def book(request: HttpRequest):
    books = Book.objects.all()
    context = {
        "books": books,
    }
    return render(request, 'book/book.html', context=context)
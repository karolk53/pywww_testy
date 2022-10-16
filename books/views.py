from django.shortcuts import render
from django.template import loader
from .models import Book

# Create your views here.
def books_list(request):
    books_list = Book.objects.all()
    context = {'books': books_list}
    return render(request,"books/books_list.html",context)
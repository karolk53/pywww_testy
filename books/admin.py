from django.contrib import admin
from books.models import Book

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title","author","available"]
    search_fields = ["title","author","description"]
    list_filter = ["available"]
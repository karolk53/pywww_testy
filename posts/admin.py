from django.contrib import admin
from .models import Posts
# Register your models here.

@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id","title","created","modified","published","sponsored"]
    search_fields = ["title"]
    list_filter = ["published","sponsored"]
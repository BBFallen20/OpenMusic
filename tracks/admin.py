from django.contrib import admin
from .models import Track, Genre, Author


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'genre', 'author']
    ordering = ['-title']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['-name']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    ordering = ['-last_name']

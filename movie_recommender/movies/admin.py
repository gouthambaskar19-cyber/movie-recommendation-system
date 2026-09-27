from django.contrib import admin
from .models import Movie

admin.site.site_header = 'Movie Recommendation System'
admin.site.site_title = 'Movie Recommendation System'
admin.site.register(Movie)

# Register your models here.

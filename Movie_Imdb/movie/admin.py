from django.contrib import admin
from .models import Movie,Genre
# Register your models here.
admin.site.register((Movie,Genre))

from unittest.util import _MAX_LENGTH
from django.contrib import admin
from .models import *

admin.site.register(Post)
admin.site.register(Libro)
admin.site.register(Pelicula)
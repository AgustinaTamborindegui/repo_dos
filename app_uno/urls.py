from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("lecturas", views.lecturas, name="lecturas"),
    path("peliculas", views.peliculas, name="peliculas"),
    path("post", views.post, name="post"),
    path("alta_lecturas", views.alta_lecturas, name="alta_lecturas"),
    path("alta_peliculas", views.alta_peliculas, name="alta_peliculas"),
    path("alta_post", views.alta_post, name="alta_post"),
    path("buscar_libro", views.buscar_libro ),
    path("buscar", views.buscar)

    
]
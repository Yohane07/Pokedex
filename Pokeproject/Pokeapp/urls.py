from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name="test"),
    path('index/', views.getPokemon, name="pokemon"),
    path('index/', views.setLanguage, name="language"),
    path('index/<id:id>/', views.getPokemonDetails(id=1), name="details"),
]
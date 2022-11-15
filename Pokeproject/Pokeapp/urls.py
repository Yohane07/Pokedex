from pickle import GET
from django.urls import path
from requests import get
from . import views

urlpatterns = [
    path('test/', views.test, name="test"),
    path('pokemons/', views.getPokemons, name="pokemonsList"),
    path('index/', views.setLanguage, name="language"),
    path('pokemons/1/', views.getPokemonDetails, name="pokemonDetails"),
    #path('pokemons/<id:id>/', views.getPokemonDetails(id=1), name="pokemonDetails"),
    #path('pokemons/<int:id>/', views.getPokemonDetails(get, 1), name="pokemonDetails"),
    path('', views.index, name= 'index'),
]
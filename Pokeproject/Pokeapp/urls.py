from pickle import GET
from django.urls import path
from requests import get
from . import views

urlpatterns = [
    path('pokemons/', views.getPokemons, name="pokemonsList"),
    path('index/', views.setLanguage, name="language"),
    path('pokemons/<str:name>/', views.getPokemonDetails, name="pokemonDetails"),
    path('', views.search, name="search"),
    path('pokemonEquipe/', views.getPokemonEquipe, name="pokemonEquipe"),
    #path('', views.search, name="searchPokemon2"),
]
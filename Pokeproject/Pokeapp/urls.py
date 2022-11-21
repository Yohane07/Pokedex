from pickle import GET
from django.urls import path
from requests import get
from . import views

urlpatterns = [
    path('pokemons/', views.getPokemons, name="pokemonsList"),
    path('pokemons/<str:name>/', views.getPokemonDetails, name="pokemonDetails"),
    path('', views.search, name="search"),
    path('pokemonEquipe/', views.getPokemonEquipe, name="pokemonEquipe"),
    path('addPokemonEquipe/<str:name>', views.addPokemonEquipe, name='addPokemonEquipe')]
from django.shortcuts import HttpResponse, render

# Create your views here.
def test(request):
    text = {"Oiseau":"pigeon"}
    return render(request, 'test.html', text)

import requests

def setLanguage(request):
    response_language = requests.get("https://pokeapi.co/api/v2/language/5/")
    if response_language.status_code == 200:
        content_language = response_language.json()
        return render(request, 'index.html', content_language)

def getPokemons(request):
    response_pokemon = requests.get("https://pokeapi.co/api/v2/pokemon?offset=0&limit=151")
    if response_pokemon.status_code == 200:
        content_pokemon = response_pokemon.json()
        return render(request, 'pokemonsList.html', content_pokemon)

def getPokemonDetails(request):
    #print("coucou")
    response_pokemon = requests.get("https://pokeapi.co/api/v2/pokemon?offset=0&limit=151")
    if response_pokemon.status_code == 200:
        content_pokemon = response_pokemon.json()
    response_details = requests.get("https://pokeapi.co/api/v2/pokemon/1")
    if response_details.status_code == 200:
        content_details = response_details.json()
        content_details = content_details.copy()
        content_details.update(content_pokemon)
        return render(request, 'pokemonDetails.html', content_details)

#getPokemonDetails(1, 1)
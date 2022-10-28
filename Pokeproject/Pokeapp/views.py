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

def getPokemon(request):
    response_pokemon = requests.get("https://pokeapi.co/api/v2/pokemon?offset=0&limit=151")
    if response_pokemon.status_code == 200:
        content_pokemon = response_pokemon.json()
        return render(request, 'index.html', content_pokemon)

def getPokemonDetails(request, id):
    #id = self.kwargs['id']
    response_details = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(id))
    if response_details.status_code == 200:
        content_details = response_details.json()
        return render(request, 'index.html', content_details)
    
#getPokemonDetails(1)
from django.shortcuts import HttpResponse, render
import requests
import urllib.request
import json

# Create your views here.
def getTypesByName(name):
    response_details = requests.get("https://pokeapi.co/api/v2/pokemon/" + name)
    if response_details.status_code == 200:
        content_details = response_details.json()
        type_name = []
        for type in content_details['types']:
            type_name += [type['type']['name']]
    return type_name

def getPokemons(request):
    response_pokemon = requests.get("https://pokeapi.co/api/v2/pokemon?offset=0&limit=151")
    if response_pokemon.status_code == 200:
        content_pokemon = response_pokemon.json()
        for pokemon in content_pokemon['results']:
            name = pokemon['name']
            pokemon['types'] = getTypesByName(name)
        return render(request, 'pokemonsList.html', content_pokemon)

def getPokemonEquipe(request):
    return render(request,'pokemonEquipe.html')

def getPokemonDetails(request, name):
    response_details = requests.get("https://pokeapi.co/api/v2/pokemon/" + name)
    if response_details.status_code == 200:
        content_details = response_details.json()
        return render(request, 'pokemonDetails.html', content_details)

def addPokemonEquipe(request, name):
    if equipePokemon in locals():
        equipePokemon.append(name)
    else:
        equipePokemon  = []
        equipePokemon.append(name)
    return render(request, 'pokemonEquipe.html', equipePokemon)
    
def search(request):
    if request.method == 'POST':
        pokemon = request.POST['pokemon'].lower()
        pokemon = pokemon.replace('%20', '')
        url_pokeapi = urllib.request.Request(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")
        url_pokeapi.add_header('User-Agent', 'pokemon')

        source = urllib.request.urlopen(url_pokeapi).read()

        list_of_data = json.loads(source)
        
        data = {
            "id": str(list_of_data['id']),
            "name": str(list_of_data['name']),
            "order": str(list_of_data['order']),
            "height": str(list_of_data['height']),
            "weight":str(list_of_data['weight']),
            "sprite": str(list_of_data['sprites']['other']['dream_world']['front_default']),
        }
    else:
        data = {}
        return render(request, 'search.html', data)
    

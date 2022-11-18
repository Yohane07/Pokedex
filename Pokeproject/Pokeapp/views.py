from django.shortcuts import HttpResponse, render
import requests
import urllib.request
import json

# Create your views here.
def setLanguage(request):
    response_language = requests.get("https://pokeapi.co/api/v2/language/5/")
    if response_language.status_code == 200:
        content_language = response_language.json()
        return render(request, 'index.html', content_language)

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

def getPokemonDetails(request, name):
    response_details = requests.get("https://pokeapi.co/api/v2/pokemon/" + name)
    if response_details.status_code == 200:
        content_details = response_details.json()
        return render(request, 'pokemonDetails.html', content_details)
    
def search(request):
    if request.method == 'POST':
        pokemon = request.POST['pokemon'].lower()
        pokemon = pokemon.replace('%20', '')
        url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokemon/{pokemon}/')
        url_pokeapi.add_header('User-Agent', 'charmander') # mettre pokemon à la place de charmander

        source = urllib.request.urlopen(url_pokeapi).read()

        list_of_data = json.loads(source)

        data = {
            "number": str(list_of_data['id']),
            "name": str(list_of_data['name']),
            "height": str(list_of_data['height']),
            "weight":str(list_of_data['weight']),
            "sprite": str(list_of_data['sprites']['front_default']),
        }

        print(data)

    else:
        data = {}

    #return render(request, 'index.html', data)
    return render(request, 'pokemonsList.html', data)
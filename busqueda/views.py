from django.http import HttpResponse
from django.shortcuts import render
import requests
import json
import matplotlib.pyplot as plt

# Create your views here.
def index(*args, **kwars):
    return HttpResponse("<img src='https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png' alt='MDN'>")




def buscarPokemon(request):
    url = 'https://pokeapi.co/api/v2/pokemon/'
    nombre=request.POST
    peticion = requests.get(url + str(nombre))
    respuesta = json.loads(peticion.content)

    pokemon_data = {
    'name': '',
    
    'abilities': '',
    
    'sprites': ''
    }
    
    pokemon_data['name'] = respuesta['name']
    pokemon_data['abilities'] = respuesta['abilities']
    pokemon_data['sprites'] = respuesta['sprites']['other']['official-artwork']['front_default']
 
    # print(pokemon_data)
    return pokemon_data




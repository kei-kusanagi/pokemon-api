from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
import requests
import json


# Create your views here.
def index(*args, **kwars):
    return HttpResponse("<img src='https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png' alt='MDN'>")




def buscarPokemon(request):
    url = 'https://pokeapi.co/api/v2/pokemon/'
    # nombre=request.POST
    nombre='rayquaza'
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
    poke_imagen = pokemon_data['sprites']
    imagen = {'imagen': poke_imagen}
 
    
    return render(request, 'busqueda.html', imagen)




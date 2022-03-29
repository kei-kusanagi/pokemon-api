from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

import json


# Create your views here.
def index(request):
    queryset = request.GET.get('busqueda')
    if queryset:
        url = 'https://pokeapi.co/api/v2/pokemon/'
        nombre=queryset
        
        peticion = request.get(url + str(nombre))
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
        return render(request, 'index.html')
    
        
    else:
        print("no encontrado)")

    return render(request, 'index.html')




def buscarPokemon(request):
    
    url = 'https://pokeapi.co/api/v2/pokemon/'
    
    nombre=request.POST
    
    peticion = request.get(url + str(nombre))
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
 
    
    return render(request, 'busqueda.html')




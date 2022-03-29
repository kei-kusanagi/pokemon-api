from urllib import request
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from pprint import pprint
import json
import requests


# Create your views here.
def index(request):
    queryset = request.GET.get('busqueda')
    # print("request")
    # pprint(request)
    # print("request.GET")
    # pprint(request.GET)
    if queryset:
        url = 'https://pokeapi.co/api/v2/pokemon/'
        nombre=str(queryset)
        link = url + nombre
        peticion = requests.get(link)
        # print("peticion imagen de del poquemon buscado")
        # pprint(peticion)
        if peticion.status_code == 200:
            # print("peticion")
            # pprint(peticion)
            respuesta = peticion.json()
            # print("respuesta")
            # pprint(respuesta)
            pokemon_data = {
            'name': '',
            
            'abilities': '',
            
            'sprites': ''
            }
            
            pokemon_data['name'] = respuesta['name']
            pokemon_data['abilities'] = respuesta['abilities']
            pokemon_data['sprites'] = respuesta['sprites']['other']['official-artwork']['front_default']
            poke_imagen = pokemon_data['sprites']
            poke_nombre = pokemon_data['name']
            imagen = {'imagen': poke_imagen, 'nombre': poke_nombre}
            # nombre = {'nombre': poke_nombre}
            
            
            return render(request, 'index.html', imagen)
        else:
            # print("no encontro el pokemon")
            poke_imagen="static/img/404.png"
            imagen = {'imagen': poke_imagen}
            
            return render(request, 'index.html', imagen)
    
        
    else:
        # print("imagen de pikachu y eevee")
        poke_imagen="static/img/buscar.png"
        
        imagen = {'imagen': poke_imagen}
        return render(request, 'index.html', imagen)

    




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




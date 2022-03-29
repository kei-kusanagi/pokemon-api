from urllib import request
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from pprint import pprint
import json
import requests


# Create your views here.
def index(request):
    queryset = request.GET.get('busqueda')
    print("request")
    pprint(request)
    print("request.GET")
    pprint(request.GET)
    if queryset:
        url = 'https://pokeapi.co/api/v2/pokemon/'
        nombre=str(queryset)
        link = url + nombre
        peticion = requests.get(link)
        print("peticion imagen de del poquemon buscado")
        pprint(peticion)
        if peticion.status_code == 200:
            print("peticion")
            pprint(peticion)
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
            imagen = {'imagen': poke_imagen}
            print("imagen")
            pprint(imagen)
            
            return render(request, 'index.html', imagen)
        else:
            print("no encontro el pokemon")
            poke_imagen="https://p4.wallpaperbetter.com/wallpaper/732/308/18/art-pokemon-illustration-minimalism-pikachu-hd-wallpaper-preview.jpg"
            imagen = {'imagen': poke_imagen}
            return render(request, 'index.html', imagen)
    
        
    else:
        print("imagen de pikachu y eevee")
        poke_imagen="https://gaminguardian.com/wp-content/uploads/2018/03/DY-O7RqWsAApCSb.jpg"
        print("no encontrado")
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




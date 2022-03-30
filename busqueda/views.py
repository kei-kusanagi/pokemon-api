from unicodedata import name
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
            
            respuesta = peticion.json()
            pokemon_data = {
            'name': '',
            'abilitie_desc': '',
            'abilitie_name': '',
            'sprites': ''
            }

            pokemon_data['name'] = respuesta['name'].upper()
            
            
            pokemon_data['sprites'] = respuesta['sprites']['other']['official-artwork']['front_default']
            for n in respuesta['abilities']:
                
                url_ability = n['ability']['url']
                name_ability = n['ability']['name']
                pokemon_data['abilitie_name'] = name_ability

                pokemon_data['abilitie_desc'] = requests.get(url_ability)
            
            # peticion_ability = request.get(url_ability)
            # print("url ability")
            # pprint(peticion_ability)
                



            return render(request, 'index.html', pokemon_data)
            
        else:
            
            poke_imagen="static/img/404.png"
            pokemon_data = {'sprites': poke_imagen}
            
            return render(request, 'index.html', pokemon_data)
    
        
    else:
        # imagen de pikachu y eevee
        poke_imagen="static/img/buscar.png"
        
        pokemon_data = {'sprites': poke_imagen}
        return render(request, 'index.html', pokemon_data)

    




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




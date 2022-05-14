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

    if queryset:
        url = 'https://pokeapi.co/api/v2/pokemon/'
        nombre=str(queryset)
        nombre=nombre.lower()
        link = url + nombre
        peticion = requests.get(link)
        
        if peticion.status_code == 200:
            
            respuesta = peticion.json()
            pokemon_data = {
            'name': '',
            'abilitie_desc': '',
            'abilitie_name': '',
            'sprites': '',
            'favicon': '',
            'front_default':'',
            'types':'',
            'front_shiny':'',
            'pokemon_type': '',
            'id':''
            }
            pokemon_type=[]

            pokemon_data['name'] = respuesta['name'].upper()
            pokemon_data['types'] = respuesta['types']
            
            pokemon_data['sprites'] = respuesta['sprites']['other']['official-artwork']['front_default']
            pokemon_data['favicon'] = respuesta['sprites']['front_default']
            pokemon_data['front_default'] = respuesta['sprites']['other']['home']['front_default']
            pokemon_data['front_shiny'] = respuesta['sprites']['other']['home']['front_shiny']
            pokemon_data['id'] = respuesta['id']
            print("icono")
            print(pokemon_data['favicon'])
            
            for n in respuesta['abilities']:
                print(n)
                url_ability = n['ability']['url']
                name_ability = n['ability']['name']
                pokemon_data['abilities'] =(name_ability,url_ability)

                descripcion = requests.get(url_ability)
                descripcion= descripcion.json()
                pokemon_data['abilitie_desc'] = descripcion['flavor_text_entries'][13]['flavor_text']
            # me quede aqui, falta hacer un bucle for para dividir todas las habilidades igualititito a los tipos

            for t in respuesta['types']:
                
                name_type = t['type']['name']
                pokemon_type.append(name_type)

            pokemon_data['pokemon_type']=pokemon_type
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




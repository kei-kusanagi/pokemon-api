import requests
import json
# import imutils
# import cv2
import matplotlib.pyplot as plt


url = 'https://pokeapi.co/api/v2/pokemon/'
def buscarPokemon():
    nombre=input("Que pokemon quieres ver: ")
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

    # image_url = respuesta['sprites']['other']['official-artwork']['front_default']
    # image = cv2.imread(pokemon_data['sprites'])
    # cv2.imshow('hola', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # image = io.imread(image_url)
    # io.imshow(image)
    # io.show()
    
    # plt.imshow('https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/384.png')
    # plt.show()
    
    print(pokemon_data)


buscarPokemon()



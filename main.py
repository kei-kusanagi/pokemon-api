import requests



url = 'https://pokeapi.co/api/v2/pokemon/'

response = requests.get(url)

print(response)

if response.status_code == 200:
    
    payload= response.json()

    results = payload.get('results')

    print(results)

    # for pokemon in results:
    #     name = pokemon('name')
    #     print(name)
else:
    print("Error")
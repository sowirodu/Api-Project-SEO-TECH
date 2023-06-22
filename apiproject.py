import requests

response = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
pokemon_data = response.json()

if 'abilities' in pokemon_data:
    abilities = pokemon_data['abilities']
    print("Ditto's Abilities:")
    for ability in abilities:
        ability_name = ability['ability']['name']
        print(ability_name)
else:
    print("No abilities found for Ditto.")
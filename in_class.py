import requests

def get_pokemon_data(pokemon_identifier):
    """
    Get Pokemon data from PokeAPI and extract game-relevant information

    Args:
        pokemon_identifier: Pokemon name (str) or ID (int)

    Returns:
        dict: Pokemon information with keys: name, id, hp, attack, sprite_url, type
        None: if Pokemon not found or error occurred
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_identifier}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            pokemon_info = {
                'name': data['name'],
                'id': data['id'],
                'hp': data['stats'][0]['base_stat'],
                'attack': data['stats'][1]['base_stat'],
                'sprite_url': data['sprites']['other']['dream_world']['front_default'],
                'type': data['types'][0]['type']['name']
            }
            return pokemon_info
        else:
            return None
    except Exception:
        return None

test_pokemon = ["bulbasaur", "charmander", "squirtle", 25, "pikachu"]

for pokemon in test_pokemon:
    print(f"\n--- Testing {pokemon} ---")
    data = get_pokemon_data(pokemon)
    if data:
        print(f"Found: {data['name']} (ID: {data['id']})")
        print(f"   HP: {data['hp']}, Attack: {data['attack']}")
        print(f"   Type: {data['type']}")
        print(f"   Sprite: {data['sprite_url']}")
    else:
        print(f"Failed to get data for {pokemon}")

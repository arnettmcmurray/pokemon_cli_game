# pokemon_evolution.py

from in_class import get_pokemon_data  # reuse API fetch

class EvolutionHandler:
    def __init__(self):
        self.evolution_map = {
            "bulbasaur": {"level": 16, "evolve_to": "ivysaur"},
            "charmander": {"level": 16, "evolve_to": "charmeleon"},
            "squirtle": {"level": 16, "evolve_to": "wartortle"},
        }

def check_and_evolve(self, pokemon):
    name = pokemon.name.lower()
    if name in self.evolution_map:
        evo_data = self.evolution_map[name]
        if pokemon.level >= evo_data["level"]:
            new_form = evo_data["evolve_to"]
            print(f"{pokemon.name} is evolving into {new_form}!")
            data = get_pokemon_data(new_form)
            if data:
                # Update Pokémon attributes
                pokemon.name = data["name"]
                pokemon.id = data["id"]
                pokemon.hp = data["hp"]
                pokemon.attack = data["attack"]
                pokemon.sprite_url = data["sprite_url"]
                pokemon.ptype = data["type"]
                print(f"Congrats! Your Pokemon evolved into {pokemon.name}!")

                # RECURSIVE CALL: Check if this new form can evolve further
                return self.check_and_evolve(pokemon)  # <---- beastmode

            else:
                print("Evolution failed: API data missing.")
            return True
    return False


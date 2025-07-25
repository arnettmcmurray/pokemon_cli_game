import random
from in_class import get_pokemon_data  # assumes this exists and works
from pokemon import Pokemon            # assumes this exists and works

class PokemonGame:
    def __init__(self, player):
        self.player = player          # your Player object with add/remove/show methods
        self.wild_pokemon = None

    def go_hunting(self):
        # Part 1: Generate wild Pokemon
        random_id = random.randint(1, 151)
        data = get_pokemon_data(random_id)
        if data:
            self.wild_pokemon = Pokemon(
                name=data['name'],
                id=data['id'],
                hp=data['hp'],
                attack=data['attack'],
                sprite_url=data['sprite_url'],
                ptype=data['type']
            )
        else:
            print("Failed to find any wild Pokemon right now.")
            return

        # Part 2: Encounter menu
        print(f"\nA wild {self.wild_pokemon.name} appeared!")
        self.wild_pokemon.info()
        print("\n1. Try to catch  2. Flee")
        choice = input("What do you want to do? ").strip()
        if choice == "1":
            self.try_catch_pokemon()
        else:
            print(f"You fled from {self.wild_pokemon.name}.\n")
            self.wild_pokemon = None

def try_catch_pokemon(self):
    base_catch_rate = 0.25
    # Catch rate is harsh at ~25%. Brutal luck.
    # Maybe our dev will hook us up with some fruit mechanics soon—
    # berries to sweeten the deal and entice those wild Pokémon.

    print("\nYou throw a Pokeball...")
    print(f"Catch rate: {base_catch_rate * 100}%")
    roll = random.random()
    if roll <= base_catch_rate:
        if self.player.add_pokemon(self.wild_pokemon):
            print(f"Gotcha! {self.wild_pokemon.name} was caught!")
        else:
            print("Your collection is full! Can't catch more Pokemon.")
        self.wild_pokemon = None
    else:
        print(f"Oh no! {self.wild_pokemon.name} escaped!\n")



    def remove_pokemon_menu(self):
        print("\nYour current Pokemon collection:")
        self.player.show_collection()
        choice = input("Enter the number of the Pokemon to remove (or anything else to cancel): ").strip()
        if not choice.isdigit():
            print("Canceling removal.")
            return
        index = int(choice) - 1
        if index < 0 or index >= len(self.player.collection):
            print("Invalid selection. Canceling removal.")
            return
        removed = self.player.remove_pokemon(index)
        if removed:
            print(f"Removed {removed.name} from your collection.\n")
        else:
            print("Failed to remove Pokemon.\n")

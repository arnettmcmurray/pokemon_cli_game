from player import Player
from pokemon_game import PokemonGame
from in_class import get_pokemon_data
from pokemon import Pokemon

from team import Team
from pokemon_evolution import EvolutionHandler

def choose_starter(player, team):
    starters = {
        "1": "bulbasaur",
        "2": "charmander",
        "3": "squirtle"
    }
    print("Choose your starter Pokemon:")
    print("1. Bulbasaur (Grass type)")
    print("2. Charmander (Fire type)")
    print("3. Squirtle (Water type)")

    while True:
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice in starters:
            data = get_pokemon_data(starters[choice])
            starter = Pokemon(
                name=data['name'],
                id=data['id'],
                hp=data['hp'],
                attack=data['attack'],
                sprite_url=data['sprite_url'],
                ptype=data['type']
            )
            player.add_pokemon(starter)
            team.add_member(starter)  # Add starter to team as well
            print(f"\n{starter.name.capitalize()} added to your collection and team!")
            print(f"You chose {starter.name.capitalize()}! Great choice!\n")
            break
        else:
            print("Invalid choice, try again.")

def evolve_pokemon_on_team(team, evo_handler):
    pokemon_name = input("Enter the name of the Pokémon to evolve: ").strip()
    for p in team.members:
        if p.name.lower() == pokemon_name.lower():
            evolved = evo_handler.check_and_evolve(p)
            if evolved:
                print(f"{p.name} has evolved successfully in your team!")
            else:
                print(f"{p.name} could not evolve.")
            return
    print(f"No Pokémon named {pokemon_name} found in your team.")

def manage_team(team, evo_handler):
    while True:
        print("\n--- Team Management ---")
        print("1. View team members")
        print("2. Add Pokémon to team")
        print("3. Remove Pokémon from team")
        print("4. Evolve a Pokémon")
        print("5. Back to main menu")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            team.list_members()
        elif choice == "2":
            name = input("Enter the name of the Pokémon to add: ").strip()
            # Here, add logic to check if player has this pokemon in collection to add
            print("Feature to add Pokémon from collection to team coming soon.")
        elif choice == "3":
            name = input("Enter the name of the Pokémon to remove: ").strip()
            team.remove_member(name)
        elif choice == "4":
            evolve_pokemon_on_team(team, evo_handler)
        elif choice == "5":
            break
        else:
            print("Invalid choice, try again.")

def main():
    print("Welcome to Pokemon CLI Adventure!")
    name = input("What's your name, trainer? ").strip()
    player = Player(name)
    game = PokemonGame(player)

    team = Team(f"{name}'s Team")
    evo_handler = EvolutionHandler()

    print(f"\nHello {name}! Time to choose your starter Pokemon!\n")
    choose_starter(player, team)

    while True:
        print(f"=== Pokemon Adventure - {name} ===")
        print("1. Go hunting (find wild Pokemon)")
        print("2. View your collection")
        print("3. Remove Pokemon from collection")
        print("4. Manage team (add/remove/evolve)")
        print("5. Quit game")

        choice = input("What would you like to do? ").strip()
        if choice == "1":
            game.go_hunting()
        elif choice == "2":
            player.show_collection()
        elif choice == "3":
            game.remove_pokemon_menu()
        elif choice == "4":
            manage_team(team, evo_handler)
        elif choice == "5":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()

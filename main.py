from player import Player
from pokemon_game import PokemonGame
from in_class import get_pokemon_data
from pokemon import Pokemon

def choose_starter(player):
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
            print(f"\n{starter.name.capitalize()} added to your collection!")
            print(f"You chose {starter.name.capitalize()}! Great choice!\n")
            break
        else:
            print("Invalid choice, try again.")

def main():
    print("Welcome to Pokemon CLI Adventure!")
    name = input("What's your name, trainer? ").strip()
    player = Player(name)
    game = PokemonGame(player)

    print(f"\nHello {name}! Time to choose your starter Pokemon!\n")
    choose_starter(player)

    while True:
        print(f"=== Pokemon Adventure - {name} ===")
        print("1. Go hunting (find wild Pokemon)")
        print("2. View your collection")
        print("3. Remove Pokemon from collection")
        print("4. Quit game")

        choice = input("What would you like to do? ").strip()
        if choice == "1":
            game.go_hunting()
        elif choice == "2":
            player.show_collection()
        elif choice == "3":
            game.remove_pokemon_menu()
        elif choice == "4":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()

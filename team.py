# teams.py

class Team:
    def __init__(self, name):
        self.name = name
        self.members = []  # list of pokemon objects or dicts

    def add_member(self, pokemon):
        if pokemon not in self.members:
            self.members.append(pokemon)
            print(f"{pokemon.name} added to team {self.name}.")
        else:
            print(f"{pokemon.name} is already on the team.")

    def remove_member(self, pokemon_name):
        for p in self.members:
            if p.name == pokemon_name:
                self.members.remove(p)
                print(f"{pokemon_name} removed from team {self.name}.")
                return
        print(f"{pokemon_name} not found on team {self.name}.")

    def list_members(self):
        if not self.members:
            print(f"Team {self.name} has no members.")
            return
        print(f"Team {self.name} members:")
        for p in self.members:
            print(f"- {p.name} (Level {p.level})")

class Player:
    def __init__(self, name, max_collection=6):
        self.name = name
        self.collection = []
        self.max_collection = max_collection

    def add_pokemon(self, pokemon):
        if len(self.collection) >= self.max_collection:
            return False
        self.collection.append(pokemon)
        return True

    def remove_pokemon(self, index):
        if 0 <= index < len(self.collection):
            return self.collection.pop(index)
        return None

    def show_collection(self):
        if not self.collection:
            print("Your collection is empty.")
            return
        for i, p in enumerate(self.collection, 1):
            print(f"{i}. {p.name.capitalize()} (Level {p.level})")

class Pokemon:
    def __init__(self, name, id, hp, attack, sprite_url, ptype, level=1):
        self.name = name
        self.id = id
        self.hp = hp
        self.attack = attack
        self.sprite_url = sprite_url
        self.ptype = ptype
        self.level = level

    def info(self):
        print(f"{self.name.capitalize()} (ID: {self.id})")
        print(f"   HP: {self.hp}")
        print(f"   Attack: {self.attack}")
        print(f"   Type: {self.ptype}")
        print(f"   Sprite: {self.sprite_url}")

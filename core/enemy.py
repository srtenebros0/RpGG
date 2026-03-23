import random
from random import choice

class Enemy:
    def __init__(self, player_level):
        scale = 1 + (player_level * 0.2)
        enemy_type = random.choice(["TANQUE", "AGRESIVO", "BALANCEADO"])

        if enemy_type == "TANQUE":
            self.name = "Golem de Obsidiana"
            self.hp = int(random.randint(90, 120) * scale)
            self.max_hp = self.hp
            self.attack = int(random.randint(4, 8) + scale)
            self.xp_reward = int(random.randint(30, 50) * scale)
            self.gold_reward = int(random.randint(10,30) * scale)
            self.loot_table = [
                {"name": "Armadura", "type": "armor", "hp": 15},
                {"name": "Poción", "type": "consumable", "heal": 20}
            ]

        elif enemy_type == "AGRESIVO":
            self.name = "Druida Oscuro"
            self.hp = int(random.randint(40, 70) * scale)
            self.max_hp = self.hp
            self.attack = int(random.randint(10, 18) * scale)
            self.xp_reward = int(random.randint(25, 45) * scale)
            self.gold_reward = int(random.randint(10, 30) * scale)
            self.loot_table = [
                {"name": "Espada", "type": "weapon", "attack": 5},
                {"name": "Poción", "type": "consumable", "heal": 20}
            ]

        else:
            self.name = "Valkiria"
            self.hp = int(random.randint(60,90) * scale)
            self.max_hp = self.hp
            self.attack = int(random.randint(6,12) * scale)
            self.xp_reward = int(random.randint(20,40) * scale)
            self.gold_reward = int(random.randint(10, 30) * scale)
            self.loot_table = [
                {"name": "Espada", "type": "weapon", "attack": 5},
                {"name": "Armadura", "type": "armor", "hp": 15},
                {"name": "Poción", "type": "consumable", "heal": 20}
            ]

        self.type = enemy_type
        self.behavior = enemy_type
        self.status_effects = []

    def is_alive(self):
        return self.hp > 0
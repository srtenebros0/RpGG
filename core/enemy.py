import random
from random import choice


class Enemy:
    def __init__(self):
        enemy_type = random.choice(["TANQUE", "AGRESIVO", "BALANCEADO"])

        if enemy_type == "TANQUE":
            self.name = "Golem de Obsidiana"
            self.hp = random.randint(90, 120)
            self.max_hp = self.hp
            self.attack = random.randint(4,8)
            self.xp_reward = random.randint(30, 50)
            self.gold_reward = random.randint(10,30)
            self.loot_table = [
                {"name": "Armadura", "type": "armor", "hp": 15},
                {"name": "Poción", "type": "consumable", "heal": 20}
            ]

        elif enemy_type == "AGRESIVO":
            self.name = "Druida Oscuro"
            self.hp = random.randint(40, 70)
            self.max_hp = self.hp
            self.attack = random.randint(10, 18)
            self.xp_reward = random.randint(25, 45)
            self.gold_reward = random.randint(10, 30)
            self.loot_table = [
                {"name": "Espada", "type": "weapon", "attack": 5},
                {"name": "Poción", "type": "consumable", "heal": 20}
            ]

        else:
            self.name = "Valkiria"
            self.hp = random.randint(60,90)
            self.max_hp = self.hp
            self.attack = random.randint(6,12)
            self.xp_reward = random.randint(20,40)
            self.gold_reward = random.randint(10, 30)
            self.loot_table = [
                {"name": "Espada", "type": "weapon", "attack": 5},
                {"name": "Armadura", "type": "armor", "hp": 15},
                {"name": "Poción", "type": "consumable", "heal": 20}
            ]

        self.type = enemy_type
        self.behavior = enemy_type

    def is_alive(self):
        return self.hp > 0
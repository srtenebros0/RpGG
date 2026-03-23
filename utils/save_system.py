import json
import os

#SAVE_FILE = "save.json"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_FILE = os.path.join(BASE_DIR, "..", "save.json")

def save_game(player):
    data= {
        "name": player.name,
        "hp": player.hp,
        "base_max_hp": player.base_max_hp,
        "base_attack": player.base_attack,
        "equipment": player.equipment,
        "level": player.level,
        "xp": player.xp,
        "xp_to_next": player.xp_to_next,
        "gold": player.gold,
        "inventory": player.inventory
    }

    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

        print(f"Guardando en: {SAVE_FILE}")
        print("\n💾 PARTIDA GUARDADA...")

def load_game(Player):
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        player = Player(data["name"])
        player.hp = data["hp"]
        player.base_max_hp = data["base_max_hp"]
        player.base_attack = data["base_attack"]
        player.equipment = data["equipment"]
        player.level = data["level"]
        player.xp = data["xp"]
        player.xp_to_next = data["xp_to_next"]
        player.gold = data["gold"]
        player.inventory = data["inventory"]

        print("\n📁 PARTIDA CARGADA...")
        return player

    except FileNotFoundError:
        return None
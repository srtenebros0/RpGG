from random import choice
from utils.save_system import save_game, load_game
from core.player import Player
from core.combat import start_combat
from core.shop import open_shop
from core.equipment import equip_item
from utils.helpers import show_inventory,RARITIES,get_random_rarity, generate_item
import random
import copy

#============L O O T ===============================#
def find_loot(player):

    base_items = [
        {"name": "Espada", "type": "weapon", "attack": 5},
        {"name": "Armadura", "type": "armor", "hp": 15},
        {"name": "Poción", "type": "consumable", "heal": 20}
    ]

    base_items = random.choice(base_items)
    item = generate_item(base_items)

    rarity = get_random_rarity()

    item["rarity"] = rarity

    multiplier = RARITIES[rarity]["multiplier"]

    if item["type"] == "weapon":
        item["attack"] = int(item["attack"] * multiplier)

    elif item["type"] == "armor":
        item["hp"] = int(item["hp"] * multiplier)

    player.inventory.append(item)

    print(f"\n🎁 Encontraste: {RARITIES[item['rarity']]['label']} {item['name']}")
#============ F I N | L O O T ======================#

#============ M A I N ===============================#
def main():
    print("Bienvenido a RpGG, una aventura en texto 🔥⚔️")

    loaded_player = load_game(Player)

    if loaded_player:
        #choice = input("¿Quieres cargar la partida guardada? (S/N): ")

        #if choice == "S":
        player = loaded_player
        #else:
            #name = input("¿Como sellama tu personaje?")
            #player = Player(name)
    else:
        name = input("¿Como se llama tu personaje?")
        player = Player(name)

    while True:
        print("=========================================")
        print("\n--- EXPLORACIÓN ---")
        print(f"Nivel: {player.level} | VIDA: {player.hp}/{player.get_max_hp()} | XP: {player.xp}/{player.xp_to_next}")
        print(f"Oro: {player.gold}")

        print("\n1. Explorar. 🌳")
        print("2. Tienda. 🏪")
        print("3. Inventario. 🏪")
        print("4. Equipar. 💪")
        print("5. Guardar Partida. 💾")
        print("6. Salir del juego. ❌")


        choice = input("Elige una opcion: ")

        if choice == "1":
            event = random.random()
            if event < 0.6:
                start_combat(player)
            elif event < 0.85:
                find_loot(player)
            else:
                print("\nNo encontraste nada . . .")
                print("=========================================")

        elif choice == "2":
            open_shop(player)

        elif choice == "3":
            show_inventory(player)

        elif choice == "4":
            equip_item(player)

        elif choice == "5":
            save_game(player)

        elif choice == "6":
            print("\nGracias por jugar.")
            print("=========================================")
            break
        else:
            print("\nOpcion invalida 🤔.")
            print("=========================================")
#============ F I N | M A I N ===============================#

if __name__ == "__main__":
    main()


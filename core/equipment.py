from utils.helpers import RARITIES
def equip_item(player):
    if not player.inventory:
        print("\nNo tienes objetos.")
        return
    print("\n🎒 INVENTARIO")

    for i, item in enumerate(player.inventory):
        rarity = item.get("rarity", "common")
        rarity_data = RARITIES[rarity]
        print(f"{i + 1}. {rarity_data.get('icon', '')} [{rarity_data['label']}] {item['name']} ({item['type']})")
    print(f"9. SALIR ❌")

    choice = input("Elige un objeto a equipar: ")

    if not choice.isdigit():
        print("Opcion Invalida.")
        return


    index = int(choice) - 1

    if index < 0 or index >= len(player.inventory):
        print("Opcion Invalida.")
        return

    item = player.inventory[index]

    if item["type"] == "weapon":
        player.equipment["weapon"] = item
        print(f"\n⚔️ Equipaste {item['name']}")

    elif item["type"] == "armor":
        player.equipment["armor"] = item
        print(f"\n🛡️ Equipaste {item['name']}")

    else:
        print("\nNo se puede equipar ese objeto.")
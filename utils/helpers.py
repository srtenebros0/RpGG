import random

def use_potion(player):
    for i, item in enumerate(player.inventory):
        if item["type"] == "consumable":
            heal = item.get("heal", 20)

            player.hp = min(player.get_max_hp(), player.hp + heal)

            print(f"\n🧪 Usaste {item['name']} y recuperaste {heal} HP.")

            # Eliminar la poción usada
            player.inventory.pop(i)
            return True

    print("\n❌ No tienes pociones.")
    return False

def show_inventory(player):
    print("\n🎒 INVENTARIO")

    if not player.inventory:
        print("Vacío.")
        return

    for i, item in enumerate(player.inventory):
        rarity = item.get("rarity", "common")
        rarity_data = RARITIES[rarity]

        # Base del texto
        text = f"{i+1}. {rarity_data.get('icon', '')} [{rarity_data['label']}] {item['name']}"

        # Stats según tipo
        if item["type"] == "weapon":
            text += f" (+{item.get('attack', 0)} ATK)"

            if player.equipment["weapon"] == item:
                text += " ⚔️ (equipado)"

        elif item["type"] == "armor":
            text += f" (+{item.get('hp', 0)} HP)"

            if player.equipment["armor"] == item:
                text += " 🛡️ (equipado)"

        elif item["type"] == "consumable":
            text += f" (cura {item.get('heal', 0)} HP)"

        print(text)

    # 👇 info extra (muy útil)
    print("\n--- EQUIPO ACTUAL ---")

    weapon = player.equipment["weapon"]
    armor = player.equipment["armor"]

    print(f"⚔️ Arma: {weapon['name'] if weapon else 'Ninguna'}")
    print(f"🛡️ Armadura: {armor['name'] if armor else 'Ninguna'}")

RARITIES = {
    "common": {
        "multiplier": 1.0,
        "label": "Común","icon": "⚪"
    },
    "rare":{
        "multiplier": 1.5,
        "label": "Raro","icon": "🔵"
    },
    "epic": {
        "multiplier": 2.0,
        "label": "Épico","icon": "⚫"
        }
    }

def get_random_rarity():
    roll = random.random()

    if roll < 0.6:
        return "common"
    elif roll < 0.9:
        return "rare"
    else:
        return "epic"

#========== G E N E R A D O R  D E  I T E M S ===========#

WEAPON_PREFIXES = []
ARMOR_PREFIXES = []

#========== G E N E R A D O R  D E  I T E M S ===========#
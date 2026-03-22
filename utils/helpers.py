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

def drop_loot(player, enemy):
    #Elegir item base del enemigo

    base_item = random.choice(enemy.loot_table)

    #Convertirlo en item dinámico (rareza + stats)
    item = generate_item(base_item)

    #Agregar al inventario
    player.inventory.append(item)

    print(f"\n🎁 El enemigo dejó: {item['name']} ({item['rarity']})")

def show_inventory(player):
    from utils.helpers import RARITIES

    print("\n🎒 INVENTARIO")

    if not player.inventory:
        print("Vacío.")
        return

    # 🔥 Agrupar items (stack)
    grouped = {}

    for item in player.inventory:
        key = (
            item["name"],
            item["type"],
            item.get("rarity", "common")
        )

        if key not in grouped:
            grouped[key] = {
                "item": item,
                "count": 1
            }
        else:
            grouped[key]["count"] += 1

    # 🔽 Mostrar inventario agrupado
    for i, data in enumerate(grouped.values()):
        item = data["item"]
        count = data["count"]

        rarity = item.get("rarity", "common")
        rarity_data = RARITIES[rarity]

        text = f"{i+1}. {rarity_data.get('icon','')} [{rarity_data['label']}] {item['name']}"

        # Stats
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

        # 🔥 Mostrar cantidad
        if count > 1:
            text += f" x{count}"

        print(text)

    # Mostrar equipo actual
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

WEAPON_PREFIXES = ["de Fuego","del Trueno","Oscura","Sagrada","Maldita"]
ARMOR_PREFIXES = ["del Guardián","de Acero","Mística","Antigua","Maldita"]

def generate_item(base_item):
    item = base_item.copy()

    # Elegir Rareza
    rarity = get_random_rarity()
    item["rarity"] = rarity
    multiplier = RARITIES[rarity]["multiplier"]

    # Modificar stats
    if item["type"] == "weapon":
        prefix = random.choice(WEAPON_PREFIXES)
        item["name"] = f"{item['name']} {prefix}"
        item["attack"] = int(item["attack"] + multiplier)

    elif item["type"] == "armor":
        prefix = random.choice(ARMOR_PREFIXES)
        item["name"] = f"{item['name']} {prefix}"
        item["hp"] = int(item["hp"] + multiplier)

    return item

#========== G E N E R A D O R  D E  I T E M S ===========#
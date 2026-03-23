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
# ===================== I N V E N T A R I O==========================#
def show_inventory(player):
    from utils.helpers import RARITIES

    print("\n🎒 INVENTARIO")

    if not player.inventory:
        print("Vacío.")
        return

    while True:
        # =========================
        # AGRUPAR ITEMS (STACK)
        # =========================
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

        grouped_list = list(grouped.values())

        # =========================
        # MOSTRAR INVENTARIO
        # =========================
        print("\n------------------")

        for i, data in enumerate(grouped_list):
            item = data["item"]
            count = data["count"]

            rarity = item.get("rarity", "common")
            rarity_data = RARITIES[rarity]

            text = f"{i+1}. {rarity_data.get('icon','')} [{rarity_data['label']}] {item['name']}"

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

            if count > 1:
                text += f" x{count}"

            print(text)

        print("0. Salir")

        # =========================
        # SELECCIÓN
        # =========================
        choice = input("\nSelecciona un item: ")

        if not choice.isdigit():
            print("Opción inválida.")
            continue

        choice = int(choice)

        if choice == 0:
            break

        if choice < 1 or choice > len(grouped_list):
            print("Opción inválida.")
            continue

        selected_data = grouped_list[choice - 1]
        item = selected_data["item"]

        # =========================
        # ACCIONES
        # =========================
        print(f"\nSeleccionaste: {item['name']}")
        print("1. Equipar")
        print("2. Usar")
        print("3. Tirar")
        print("4. Volver")

        action = input("Elige acción: ")

        # -------------------------
        # EQUIPAR
        # -------------------------
        if action == "1":
            if item["type"] == "weapon":
                player.equipment["weapon"] = item
                print(f"⚔️ Equipaste {item['name']}")

            elif item["type"] == "armor":
                player.equipment["armor"] = item
                print(f"🛡️ Equipaste {item['name']}")

            else:
                print("No se puede equipar.")

        # -------------------------
        # USAR (POCIÓN)
        # -------------------------
        elif action == "2":
            if item["type"] == "consumable":
                for i, inv_item in enumerate(player.inventory):
                    if inv_item == item:
                        heal = inv_item.get("heal", 20)
                        player.hp = min(player.get_max_hp(), player.hp + heal)

                        print(f"🧪 Usaste {inv_item['name']} y recuperaste {heal} HP.")
                        player.inventory.pop(i)
                        break
            else:
                print("No se puede usar.")

        # -------------------------
        # TIRAR ITEM
        # -------------------------
        elif action == "3":
            confirm = input(f"¿Tirar {item['name']}? (s/n): ")

            if confirm.lower() == "s":
                for i, inv_item in enumerate(player.inventory):
                    if inv_item == item:
                        player.inventory.pop(i)
                        print(f"🗑️ Tiraste {item['name']}")
                        break

        # -------------------------
        # VOLVER
        # -------------------------
        elif action == "4":
            continue

        else:
            print("Opción inválida.")

# ===================== F I N  I N V E N T A R I O ==========================#

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
        item["defense"] = int(3 * multiplier)

    return item

#========== G E N E R A D O R  D E  I T E M S ===========#
import random
from core.enemy import Enemy
from utils.helpers import use_potion,generate_item,drop_loot

def start_combat(player):
    enemy = Enemy()

    print(f"\n⚔️ Un {enemy.name} de tipo ({enemy.type}) aparece frente a ti!!")

    while player.is_alive() and enemy.is_alive():

        print("\n--- ESTADO ---")
        print(f"{player.name} Nivel: {player.level} HP: {player.hp}/{player.get_max_hp()}")
        print(f"XP: {player.xp}/{player.xp_to_next}")
        print(f"{enemy.name} HP: {enemy.hp}")

        pociones = sum(1 for item in player.inventory if item["type"] == "consumable")
        print(f"\n🧪 POCIONES: {pociones}")

        print("\n1 - Atacar. ⚔️")
        print("2 - Curarte. ❤️‍🩹")
        print("3 - Huir. 💨")

        choice = input("Elige una opción: ")

        if choice == "1":
            # Ataque del jugador
            damage = random.randint(5, player.get_attack() )

            if random.random() < 0.2:
                damage *= 2
                print("\n💥 ¡Golpe CRÍTICO!")

            enemy.hp -= damage
            print(f"\nGolpeas al {enemy.name} por {damage} de daño. 🥵")

        elif choice == "2":
            used = use_potion(player)
            if not used:
                continue

        elif choice == "3":
            print("\nDecidiste Huir del Combate! 😑")
            break

        else:
            print("\nNo te pongas nervioso, toma una decision valida aventurero!")
            continue

        # Turno del enemigo
        if enemy.is_alive():
            raw_damage = random.randint(3, enemy.attack)

            if random.random() < 0.15:
                raw_damage *= 2
                print(f"\n⚠️ ¡El {enemy.name} hizo un golpe CRÍTICO!")

            defense = player.get_defense()

            final_damage = max(1, raw_damage - defense)

            player.hp -= final_damage

            print(f"\nEl {enemy.name} te golpea por {raw_damage} de daño 😈")
            print(f"🛡️ Reduces {defense} de daño.")
            print(f"💥 Recibes {final_damage} de daño.")

    # Resultado Final

    if player.hp <= 0:
        print(f"\n💀 Has sido papeado por {enemy.name}")
        player.hp = int(player.get_max_hp())

    elif enemy.hp <= 0:
        print(f"\n🔥 Derrotaste al {enemy.name}!")
        player.gain_xp(enemy.xp_reward)
        player.gold += enemy.gold_reward
        print(f"💰 Ganaste {enemy.gold_reward} monedas de oro.")
        drop_loot(player, enemy)

    else:
        print("\n🏃 Escapaste con vida.")
def open_shop(player):
    while True:
        print("\n🏪 TIENDA")
        print(f"Oro disponible: {player.gold}")
        print("\n1. Comprar pocion (20 oro) 🧪")
        print("2. Salir 🏃")

        choice = input("Elige una opción: ")

        if choice == "1":
            if player.gold >= 20:
                player.gold -= 20
                player.inventory.append({
                    "name": "Poción",
                    "type": "consumable",
                    "heal": 20
                })
                print("\n🧪 Compraste una poción")
            else:
                print("\n❌ No tienes suficiente oro.")
        elif choice == "2":
            print("\nSale de la tienda... Vuelva Pronto!")
            break
        else:
            print("\nOpcion Invalida")
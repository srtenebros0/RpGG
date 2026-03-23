class Player:
    def __init__(self,name):
        self.name = name
        self.hp = 100
        #self.max_hp = 100
        #self.attack = 10

        self.level = 1
        self.xp = 0
        self.xp_to_next = 50

        self.gold = 15
        self.inventory = []

        self.base_attack = 10
        self.base_max_hp = 100

        self.equipment = {
            "weapon": None,
            "armor": None
        }

        self.base_defense = 2
        self.status_effects = []

#====================================================#

#==================== A T A Q U E  P L A Y E R ======================#
    def get_attack(self):
        bonus = 0

        if self.equipment["weapon"]:
            bonus += self.equipment["weapon"].get("attack",0)
        return self.base_attack + bonus

# ==================== F U N C I O N  D E A R M O R ===========================#

    def get_defense(self):
        bonus = 0

        if self.equipment["armor"]:
            bonus += self.equipment["armor"].get("defense",0)

        return self.base_defense + bonus

# ===============================================#

# ===============================================#

    def get_max_hp(self):
        bonus = 0

        if self.equipment["armor"]:
            bonus += self.equipment["armor"].get("hp",0)
        return self.base_max_hp + bonus

# ===============================================#

    def is_alive(self):
        return self.hp > 0

# ===============================================#

    def gain_xp(self, amount):
        self.xp += amount
        print(f"\nGanaste {amount} xp!")

        if self.xp >= self.xp_to_next:
            self.level_up()

# ===============================================#

    def level_up(self):
        self.level += 1

        self.xp -= self.xp_to_next
        self.xp_to_next += 25

        self.base_max_hp += 20
        self.base_attack += 5

        self.hp = self.get_max_hp()

        print(f"\n⭐ Subiste de nivel!!")
        print(f"\nAhora eres nivel {self.level}!")
        print("Tus stats han mejorado.")
        print(f"ATAQUE: {self.get_attack()} | VIDA: {self.get_max_hp()}")
# ================================================================================#
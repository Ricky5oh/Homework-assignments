# Name: [Your Name]
# Date: [Insert Date]
# Assignment: M6A3 - Player Vs Enemy
# Description: This program creates a Player and an Enemy class to simulate combat using stats.

class Player:
    def __init__(self):
        self.name = ""
        self.health = 0
        self.damage = 0
        self.defense = 0

    def character_create(self):
        print("Please enter your player’s name:", end=" ")
        self.name = input("> ")

        self.health = self.get_valid_input("Please enter your player’s health: ")
        self.damage = self.get_valid_input("Please enter your player’s damage: ")
        self.defense = self.get_valid_input("Please enter your player’s defense: ")

        print("\nYour Player has been saved with the following information:")
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Damage: {self.damage}")
        print(f"Defense: {self.defense}\n")

    def get_valid_input(self, prompt):
        while True:
            try:
                value = int(input(prompt + " > "))
                if value < 0:
                    print("Please enter a positive number.")
                else:
                    return value
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def attack(self, enemy):
        damage_dealt = max(0, self.damage - enemy.defense)
        enemy.health = max(0, enemy.health - damage_dealt)
        print(f"{self.name} attacked the Enemy, causing {damage_dealt} damage! Enemy’s HP is now {enemy.health}!")


class Enemy(Player):
    def __init__(self):
        super().__init__()
        self.type = ""

    def character_create(self):
        types = {
            "Minion": {"health": 10, "damage": 2, "defense": 1},
            "Brawler": {"health": 30, "damage": 10, "defense": 5},
            "Elite": {"health": 100, "damage": 20, "defense": 20}
        }

        print("Please enter your enemy’s type (Minion, Brawler, Elite):", end=" ")
        while True:
            enemy_type = input("> ").capitalize()
            if enemy_type in types:
                self.type = enemy_type
                stats = types[enemy_type]
                self.health = stats["health"]
                self.damage = stats["damage"]
                self.defense = stats["defense"]
                break
            else:
                print("Invalid type. Please enter one of the following: Minion, Brawler, Elite")

        print("\nYour Enemy has been saved with the following information:")
        print(f"Type: {self.type}")
        print(f"Health: {self.health}")
        print(f"Damage: {self.damage}")
        print(f"Defense: {self.defense}\n")

    def attack(self, player):
        damage_dealt = max(0, self.damage - player.defense)
        player.health = max(0, player.health - damage_dealt)
        print(f"{self.type} attacked {player.name}, causing {damage_dealt} damage! Player’s HP is now {player.health}!")


# -------------------- Main Program Execution --------------------

print("Player VS Enemy!\n")

# Create instances
my_player = Player()
my_enemy = Enemy()

# Create characters
my_player.character_create()
my_enemy.character_create()

# Simulate attacks
my_player.attack(my_enemy)
my_enemy.attack(my_player)

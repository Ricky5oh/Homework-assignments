# Date: 08/05/25
# Homework 6:  Player VS Enemy
# Program By: Ricardo Duran
# File Name: H6_Player_V_Enemy
# Function: This program creates a Player and Enemy class to simulate a simple combat interaction.

#Setting up the player class. This function stores player's stats
class Player:
    def __init__(self):
        self.name = ""
        self.health = 0
        self.damage = 0
        self.defense = 0
    #Function for creating a player by first asking what they're name is
    def Character_create(self):
        print("Please enter your player's name:", end= '')
        self.name = input(">")

        self.health = self.get_valid_input ("Please Enter your player's health:", int)
        self.damage = self.get_valid_input ("Please Enter your player's damage:", int)
        self.defense = self.get_valid_input ("Please Enter your player's defense:", int)
        
        #Showing the stats back to the user
        print("\n Your Player has been saved with the following information:")
        print(f"Name: {self.name}")
        print(f"Health : {self.health}")
        print(f"Damage : {self.damage}")
        print(f"Defense : {self.defense}")
    
    #Ensuring that it is a positive number
    def get_valid_input(self, prompt):
        while True:
            try:
                value = int(input(prompt + " > "))
                if value < 0:
                    print("Please enter a positive number.")
                else:
                    return value
            except ValueError:
                print("Invalid input. Please Enter a valid number")
    #This function determines the enemys attack and then calculates the damage delt
    def attack(self, enemy):
        damage_dealt = max(0, self.damage - enemy.defense)
        enemy.health = max(0, enemy.health - damage_dealt)
        print(f"{self.name} attacked the Enemy, causing {damage_dealt} damage! Enemy’s HP is now {enemy.health}!")

#Created the Enemy Class
class Enemy(Player):
    def __init__(self):
        super().__init__()
        self.type = ""
    #Function to let the user pick a Enemy to attack
    def character_create(self):
        #Enemy presets
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
        #Displaying the Enemys stats
        print("\nYour Enemy has been saved with the following information:")
        print(f"Type: {self.type}")
        print(f"Health: {self.health}")
        print(f"Damage: {self.damage}")
        print(f"Defense: {self.defense}\n")
    #This function determines the player's attack and then calculates the damage delt
    def attack(self, player): 
        damage_dealt = max(0, self.damage - player.defense) 
        player.health = max(0, player.health - damage_dealt)
        print(f"{self.type} attacked {player.name}, causing {damage_dealt} damage! Player’s HP is now {player.health}!")

#main
if __name__ == "__main__":
    print("Player VS Enemy!\n")
#Creating instance of Player and Enemy
    my_player = Player()
    my_enemy = Enemy()
#Creating characters for Player and Enemy
    my_player.Character_create()
    my_enemy.Character_create()
#Calling attack function for Player and Enemy
    my_player.attack(my_enemy)
    my_enemy.attack(my_player)

    test
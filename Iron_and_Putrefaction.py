#Import the necessary libraries
import random
import time

#Def functions
def write(*text):
    print(*text)
    time.sleep(1)

def die():
    write("You died\nGAME OVER")
    write("the game close in")
    for i in range(10, 0, -1):
        print(f"{i} seconds")
        time.sleep(1)

def decide():
        decision = input("Press 'A' to atack, 'B' to block or 'E' to dodge")
        decision.upper()
        if decision =='A':
            player.attack(zombie or boss)
        elif decision == 'B':
            player.block(zombie or boss)
        elif decision == 'E':
            player.dodge(zombie or boss)
        else:
            write("invalid option")

            
#Here is where the stats are saved

class characters:
    def __init__(self, name: str, health: int, attack: int, sound: str, gold: int, defense: int):
        self.name = name
        self.health = health
        self.damage = attack
        self.sound = sound
        self.gold = gold
        self.defense = defense
    def attack (self, objective: 'characters'):
        write(self.sound)
        objective.health -= self.damage - objective.defense
        if self.health < 0:
            self.health = 0
        write(f"{self.name} attack to {objective.name}\nhas damaged {self.damage}, the defense of {objective.name} absorb {objective.defense} points of the damage of {self.name}, the attack affect to {objective.name} his life now is {objective.health}HP")
    def block(self, objective: 'characters'):
        write(f"{self.name} blocks this turn")
        write(f"{self.name} block to {objective.name}")
        
    def dodge(self, objective: 'characters'):
        write(f"{self.name} decide esquivar en este turno")
        write(f"{self.name} esquiva a {objective.name}")
    def enemyTurn():
        accionesIa = ['attack', 'block', 'dodge']
        turnoIa = random.choice(accionesIa)
        return turnoIa
        

#Here is where the shop are saved
sword_ASCII = r"""
                 /| 
                / |
               /  |
              |   |
              |   |
              |   |
              |   |
              |   |
              |   |
              |   |
        ______|___|______
       |_____       _____|
             |  _  |
             | |_| |
             \_____/
"""
potion_ASCII = r"""
          .---.
         /     \
         \_____/
         |     |
         |_____|
      .-'       '-.
     /             \
    /   .-------.   \
   /   /         \   \
  |   |---|---|---|   |
  |   | --|   |-- |   |
  |   |___|___|___|   |
  \  :::::::::::::::: /
   \ ::::::::::::::: /
    '-.___________.-'
"""
armor_ASCII = r"""
          .___________.
         /   __   __   \
        /   /  \ /  \   \

       |   |    V    |   |
    .--'---'         '---'--.
   /   _________________   \
  /   /                 \   \

 |   |     \       /     |   |
 |   |      \     /      |   |
 |   |       \   /       |   |
 |   |        \_/        |   |
  \   \                 /   /
   \   \               /   /
    `---'---._____.---'---'
"""
class shop:
    def __init__(self):
        self.catalogo = {
            "Potion": {"Nombre": "Health Potion", "Price": 10, "Art": potion_ASCII},
            "Sword": {"Nombre": "Iron Sword", "Price": 20, "Art": sword_ASCII},
            "Armor":{"Nombre": "Iron Armor", "Price": 35, "Art": armor_ASCII}
}           
    def lookShop(self):

        write("u arrived to the shop, go? 'Yes/No'")
        goShop = input().lower()

        while goShopVerify:
            if goShop == "yes":
                goShopVerify = True

            elif goShop == "no":
                goShopVerify = False

            if goShopVerify:
                for producto in self.catalogo.values():
                    print(f"{producto['Nombre']}, Cuesta {producto['Precio']} monedas")
                    write(f"{producto['Arte']}")
                    write("Press 1 for the potion, 2 for the sword, 3 for the iron armor, 4 to exit")

            elif goShopVerify == False:
                write("u skip the shop")

            else:
                write
    def buyShop(self):
        for producto in self.catalogo.values():
            print(f"{producto['Nombre']}")

#Spawnea las primeras entidades
player = characters('Talos', 100, 40, "yiaaah", 0, 10)
zombie = characters('Jhon el zombie', 100, 20, "euuegh", 25, 5)
boss = characters('Kray el paciente 0',150, 30, "ROAAAAAAR!", 100, 20)
cityShop = shop()


#HISTORY START
vueltas = 0
while vueltas < 3:

#while the player and zombie are alive, repeat the bucle
    while player.health >= 0 and zombie.health >= 0:
        decide()
        write(f"the zombie {characters.enemyTurn()} you")
        if player.health == 0:
            die()

#If the zombie dies spawn a shop
    if player.health > 0:
        cityShop.lookShop()
        num = input()
        while num != 4:
            if num == 1 and player.gold >= 10:
                print("You buy a potion")
                print("You recover 45 HP")
                player.health = min(100 , player.health + 45)
                print(player.health)

            elif player.gold < 10:
                print("You not have sufficent money")

            if num == 2 and player.gold >= 20:
                print("You buy a sword")
                player.damage += 10
                print("attack +10")
                player.damage += 10

            elif player.gold < 20:
                print("You not have sufficent gold")

            if num == 3 and player.gold >= 35:
                print("You buy an armor")
                player.defense += 20
                print("defense +20")

            elif player.gold < 35:
                print("you not have sufficent gold")

            if num == 4:
                pass
            else:
                "insert a valid number"

#Logica de lo que eliges en la tienda

    write("oh no, another zombie appears")
    zombie.health += 100
    vueltas += 1

#While the boss and player are alive, repeats the bucle

    while boss.health > 0 and player.health > 0: 
        write("attack?")
        Respuesta=str(input()).lower() 
        write(f"the big zombie shout {boss.sound}") 
        write("You have so much fear and it knows")
        Respuesta=str(input()).lower() 

        if Respuesta == "si" and player.health > 0:
            write(f"the hero say {player.sound}")
            boss.health = boss.health - player.damage
            write(f"the big zombie bleed, it lost {player.damage} HP, it keeps {max(0,boss.health)}HP")

        elif Respuesta == "no":
            write("the big zombie not have piety")

        else:  
            write("Big zombie doesnt understand your dialect")

        if boss.health > 0:
            write("it attacks you")
            player.health = max(0, player.health - boss.damage)
            write(f"Big zombie attacks you and your health down {boss.damage}HP, you have {player.health}PS")
        else:
            write("Big zombie boss is died")
            write(f"and it drop a fortune of {player.gold} gold your gold now is {player.gold + boss.gold} ")
            player.gold += boss.gold

        if player.health == 0:
            die()
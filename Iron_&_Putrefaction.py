import time
#Aqui se guardan las stats
class Personajes:
    def __init__(self, nombre: str, vida: int, ataque: int, sonido: str, oro: int, defensa: int):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.sonido = sonido
        self.oro = oro
        self.defensa = defensa
    def atacar(self,objetivo: 'Personajes'):
        mostrar(self.sonido)
        objetivo.vida -= self.ataque - objetivo.defensa
        if self.vida < 0:
            self.vida = 0
        mostrar(f"{self.nombre} ha atacado a {objetivo.nombre}\nha bajado {self.ataque}, la defensa de {objetivo.nombre} ha absorbido {objetivo.defensa} puntos del ataque de {self.nombre}, el ataque ha dejado a {objetivo.nombre} a {objetivo.vida}PS")
#Aqui se guarda todo lo que se compra en la tienda
Espada = r"""
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
Pocion = r"""
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
Armadura = r"""
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
class tienda:
    def __init__(self):
        self.catalogo = {
            "Pocion": {"Nombre": "Pocion de vida", "Precio": 10, "Arte": Pocion},
            "Espada": {"Nombre": "Espada de hierro", "Precio": 20, "Arte": Espada},
            "Armadura":{"Nombre": "Armadura de hierro", "Precio": 35, "Arte": Armadura}
}           
    def mirar_tienda(self): 
        for producto in self.catalogo.values():
            print(f"{producto['Nombre']}, Cuesta {producto['Precio']} monedas")
            print(f"{producto['Arte']}")

#Spawnea las primeras entidades
Player = Personajes('Talos', 100, 40, "yiaaah", 0, 10)
Zombie = Personajes('Jhon el zombie', 100, 20, "euuegh", 25, 5)
Boss = Personajes('Kray, el paciente 0',150, 30, "ROAAAAAAR!", 100, 20)
tiendita = tienda()

#Definir funciones de texto y pantalla de muerte
def mostrar(*texto):
    print(*texto)
    time.sleep(1.33)

def muerte():
    mostrar("has muerto\nGAME OVER")
    mostrar("el juego cerrara en")
    for i in range(10, 0, -1):
        print(f"{i} segundos")
        time.sleep(1)
#INICIO DE LA HISTORIA
mostrar("Estas perdido, no sabes donde estas") 
mostrar("te has encontrado con un zombie, te ha visto") 
mostrar(f"su vida es de {Zombie.vida}")

Zombie.atacar(Player)
vueltas = 0
while vueltas < 3:

#bucle, mientras el jugador y el Zombie esten vivos, se repite
    while Zombie.vida > 0 and Player.vida > 0: 
        mostrar("atacar?")
        Respuesta = str(input()).lower() 
        mostrar(f"Zombie dice {Zombie.sonido}") 
        if Respuesta == "si" and Player.vida > 0:
            mostrar(f"el jugador dice {Player.sonido}")
            Zombie.vida = Zombie.vida - Player.ataque
            mostrar(f"Zombie ha perdido {Player.ataque} puntos de vida, su vida restante es de {max(0,Zombie.vida)}PS")
        elif Respuesta == "no":
            mostrar("Zombie no capta tu piedad")
        else:  
            mostrar("Zombie te mira confundido")

        if Zombie.vida > 0:
            mostrar("Zombie te ataca",)
            Player.vida = max(0, Player.vida - Zombie.ataque)
            mostrar("Zombie te bajo", Zombie.ataque, "PS, te ha dejado a", Player.vida, "Puntos de vida")
        else:
            mostrar("Zombie ha caido")
            mostrar(f"tu oro pasa de {Player.oro} a {Player.oro + Zombie.oro} ")
            Player.oro += Zombie.oro

        if Player.vida == 0:
            muerte()

#Al morir el primer zombie spawnea una tienda
if Player.vida > 0:
    mostrar("has llegado a la tienda de la ciudad, ir?")
    comprar = input().lower()
    if comprar == "si":
        mostrar("BIENVENIDO A LA TIENDA")
        tiendita.mirar_tienda()
        mostrar("Presiona 1 para la pocion, 2 Para la espada, 3 Para la armadura, 4 Para salir")
        num = input()
        while num != 4:
            if num == 1:
                if Player.oro >= 10:
                    print("Has comprado una pocion")
                    print("tu vida se recupera 45 PS")
                    min(100,Player.vida) += 45
                    print(Player.vida)
                else:
                    print("no tienes suficientes monedas")
            if num == 2:
                if Player.oro >= 20:
                    print("Has comprado una Espada")
                    Player.ataque += 10
                    print("+10 de ataque")
                    Player.ataque += 10
                else:
                    print("no tienes suficientes monedas")
            if num == 3:
                if Player.oro >= 35:
                    print("Has comprado una armadura")
                    Player.defensa += 20
                    print("+20 de defensa")
                else:
                    print("no tienes suficientes monedas")
            if num == 4:
                pass
            else:
                "inserte un numero valido y vuelva a intentar"

#Logica de lo que eliges en la tienda

    mostrar("vaya, ha aparecido otro zombi")
    Zombie.vida += 100
    vueltas += 1

#bucle, mientras el jugador y el Zombie esten vivos, se repite

    while Boss.vida > 0 and Player.vida > 0: 
        mostrar("atacar?")
        Respuesta=str(input()).lower() 
        mostrar(f"el gran zombi se acerca, suelta un rugido aterrador {Boss.sonido}") 
        mostrar("Tienes mucho miedo, atacas?")
        Respuesta=str(input()).lower() 
        if Respuesta == "si" and Player.vida > 0:
            mostrar(f"el jugador dice {Player.sonido}")
            Boss.vida = Boss.vida - Player.ataque
            mostrar(f"El gran zombie ha sangrado, ha perdido {Player.ataque} puntos de vida, su vida restante es de {max(0,Boss.vida)}PS")
        elif Respuesta == "no":
            mostrar("El jefe zombie no tiene tiempo para piedad")
        else:  
            mostrar("Gran zombie no entiende tu dialecto")

        if Boss.vida > 0:
            mostrar("Esa cosa enorme te ataca")
            Player.vida = max(0, Player.vida - Boss.ataque)
            mostrar(f"El gran zombie te bajo {Boss.ataque}PS, te ha dejado a {Player.vida}PS")
        else:
            mostrar("El gran zombie ha caido")
            mostrar(f"y con el su gran fortuna, tu oro pasa de {Player.oro} a {Player.oro + Boss.oro} ")
            Player.oro += Boss.oro

        if Player.vida == 0:
            muerte()
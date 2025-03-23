﻿class Statystyki:

    def __init__(self,user, hp, atak, pieniadze):
        self.hp = hp
        self.atak = atak
        self.pieniadze = pieniadze
        self.user = user

    def __str__(self):
        return (
            f"Statystyki {self.user}:\n"
            f"HP: {self.hp}\n"
            f"Atak: {self.atak}\n"
            f"Pieniądze: {self.pieniadze}\n"
            + "-" * 20
            )

    def wyswietl_statystyki(self, nazwa):
        print(self.__str__().replace("postaci", nazwa))

    def zmien_statystyki(self, hp=0, atak=0, pieniadze=0):
        self.hp += hp
        self.atak += atak
        self.pieniadze += pieniadze
        print(f"\nZmieniono statystyki: HP {hp}, Atak {atak}, Pieniądze {pieniadze}\n")

# Tworzenie obiektów dla gracza i goblina
#gracz = Statystyki(100, 10, 50)
#goblin = Statystyki(15, 1, 5)
#ork = Statystyki(50, 5, 20)
#smok = Statystyki(200, 20, 100)

# Wyświetlanie statystyk
#gracz.wyswietl_statystyki("Gracza")
#goblin.wyswietl_statystyki("Goblina")
#ork.wyswietl_statystyki("Orka")
#smok.wyswietl_statystyki("Smoka")

# Zmiana statystyk (np. po walce)
#gracz.zmien_statystyki(hp=-10, atak=2, pieniadze=15)
#print(gracz)  # Teraz HP: 90, Atak: 12, Pieniądze: 65
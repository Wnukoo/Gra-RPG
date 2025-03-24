class Statystyki:

    # def __init__(self,user, hp, atak, pieniadze):
    #     self.hp = hp
    #     self.atak = atak
    #     self.pieniadze = pieniadze
    #     self.user = user
        

    def gracz (self):
        hp = 1000
        atak = 100
        pieniadze = 500
        print(f"Statystyki Gracza:\n")
        print(f"HP: {hp}")
        print(f"Atak: {atak}")
        print(f"Pieniądze: {pieniadze}")
        print("-" * 20)

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


# Wyświetlanie statystyk
#gracz.wyswietl_statystyki("Gracza")
#goblin.wyswietl_statystyki("Goblina")
#ork.wyswietl_statystyki("Orka")
#smok.wyswietl_statystyki("Smoka")

# Zmiana statystyk (np. po walce)
#gracz.zmien_statystyki(hp=-10, atak=2, pieniadze=15)
#print(gracz)  # Teraz HP: 90, Atak: 12, Pieniądze: 65
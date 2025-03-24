class Statystyki:
    def __init__(self, hp=100, atak=10, gold=50):
        self.hp = hp
        self.atak = atak
        self.gold = gold

    def wyswietl_statystyki(self):
        print("Statystyki Gracza:")
        print(f"HP: {self.hp}")
        print(f"Atak: {self.atak}")
        print(f"Pieniądze: {self.gold}")
        print("-" * 20)

    def up_kowal(self, kwota, atak):
        if kwota > self.gold:
            print("Nie masz tyle pieniędzy!")
            print("Zarob więcej złota!")
        else:
            print("Bron ulepszona!")
            print("Twoj atak zwiekszyl sie o 5!")
            self.gold -= kwota
            self.atak += 5
            print(f"Zostało Ci {self.gold} złota, atak zostal ulepszony o 5!")

    def up_karczma(self, hp):
        self.hp == hp
        print("Odpoczynek!")
        print(f"Twoje HP wynosi {self.hp}!")







# Wyświetlanie statystyk
#gracz.wyswietl_statystyki("Gracza")
#goblin.wyswietl_statystyki("Goblina")
#ork.wyswietl_statystyki("Orka")
#smok.wyswietl_statystyki("Smoka")

# Zmiana statystyk (np. po walce)
#gracz.zmien_statystyki(hp=-10, atak=2, pieniadze=15)
#print(gracz)  # Teraz HP: 90, Atak: 12, Pieniądze: 65
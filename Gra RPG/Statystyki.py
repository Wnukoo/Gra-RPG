class Statystyki:

    def __init__(self, hp=100, atak=10, gold=20):
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

    def up_karczma(self):
        self.hp = 100
        print("Odpoczynek!")
        print(f"Twoje HP wynosi {self.hp}!")

    def walka_Goblin(self, hp, zloto):
        atak_goblin = 15
        hp_goblin = 30
        zloto = 5
        print("Statystyki goblina:")
        print(f"HP: {hp_goblin}")
        print(f"Atak: {atak_goblin}")
        print(f"Zloto: {zloto}")
        choose = input("Czy chcesz zaatakować goblina? (T/N): ").upper()
        if choose == "T":
            if (atak_goblin >= self.hp and hp_goblin >= self.atak ):
                print("Przegrałeś!")
                print("Odpocznij w karczmie aby odzyskać siłę!")
            else:
                self.hp -= hp
                self.gold += zloto
                print(f"Twoje HP wynosi {self.hp}!")
                print(f"Zdobywasz {zloto} złota!")
        else:
            print("Uciekaj tchórzu!")

    def walka_Ork(self, hp, zloto):
        atak_ork = 30
        hp_ork = 50
        zloto = 10
        print("Statystyki Orka:")
        print(f"HP: {hp_ork}")
        print(f"Atak: {atak_ork}")
        print(f"Zloto: {zloto}")
        choose = input("Czy chcesz zaatakować Orka? (T/N): ").upper()
        if choose == "T":
            if (atak_ork >= self.hp and hp_ork >= self.atak ):
                print("Przegrałeś!")
                print("Odpocznij w karczmie aby odzyskać siłę!")
            else:
                self.hp -= hp
                self.gold += zloto
                print(f"Twoje HP wynosi {self.hp}!")
                print(f"Zdobywasz {zloto} złota!")
        else:
            print("Uciekaj tchórzu!")

    def walka_Golem(self, hp, zloto):
        atak_golem = 70
        hp_golem = 85
        zloto = 20
        print("Statystyki Orka:")
        print(f"HP: {hp_golem}")
        print(f"Atak: {atak_golem}")
        print(f"Zloto: {zloto}")
        choose = input("Czy chcesz zaatakować Orka? (T/N): ").upper()
        if choose == "T":
            if (atak_golem >= self.hp and hp_golem >= self.atak ):
                print("Przegrałeś!")
                print("Odpocznij w karczmie aby odzyskać siłę!")
            else:
                self.hp -= hp
                self.gold += zloto
                print(f"Twoje HP wynosi {self.hp}!")
                print(f"Zdobywasz {zloto} złota!")
        else:
            print("Uciekaj tchórzu!")

    def walka_Smok(self, hp, zloto):
        atak_smok = 90
        hp_smok = 150
        zloto = 100
        print("Statystki Smoka:")
        print(f"HP: {hp_smok}")
        print(f"Atak: {atak_smok}")
        print(f"Zloto: {zloto}")
        choose = input("Czy chcesz zaatakować Smoka? (T/N): ").upper()
        if choose == "T":
            if (atak_smok >= self.hp and hp_smok >= self.atak ):
                print("Przegrałeś!")
                print("Odpocznij w karczmie aby odzyskać siłę!")
            else:
                self.hp -= hp
                self.gold += zloto
                print("Pokonales bossa!")
                print(f"Zdobywasz {zloto} złota!")
                print("Koniec gry")
                print("Dziekujemy za gre!")
                print("Autor: Wnukoo")
        else:
            print("Uciekaj tchórzu!")

    def zapisz_stan(self, filename):
        with open(filename, 'w') as file:
            file.write(f"{self.hp}\n")
            file.write(f"{self.atak}\n")
            file.write(f"{self.gold}\n")
        print("Stan gry zapisany!")

    def wczytaj_stan(self, filename):
        try:
            with open(filename, 'r') as file:
                self.hp = int(file.readline().strip())
                self.atak = int(file.readline().strip())
                self.gold = int(file.readline().strip())
            print("Stan gry wczytany!")
        except FileNotFoundError:
            print("Brak pliku zapisu, zaczynasz grę od nowa.")

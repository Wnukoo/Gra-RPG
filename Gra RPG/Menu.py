from Statystyki import Statystyki
from Lokalizacje import Lokalizacje

class Menu:
    def __init__(self):
        self.gracz = Statystyki()
        self.kowal = Lokalizacje("Kowal", "Stary kowal, ktory ulepsza bron.", self.gracz)
        self.karczma = Lokalizacje("Karczma", "Karczma, gdzie mozna odpoczac.", self.gracz)
        self.polowanie = Lokalizacje("Polowanie", "Polowanie na potwory.", self.gracz)

    def menu(self):
        while True:
            print("\nWybierz co chcesz zrobic:")
            print("1 - Idz do kowala ulepszyc bron")
            print("2 - Idz do karczmy odpoczac")
            print("3 - Idz na polowanie")
            print("4 - Zobacz statystyki")
            print("5 - Wyjscie")
            print("6 - Zapisz grę")
            print("7 - Wczytaj grę")
            choose = input("Wybierz: ")
            if choose == "1":
                self.kowal.kowal()
            elif choose == "2":
                self.karczma.karczma()
            elif choose == "3":
                self.polowanie.polowanie()
            elif choose == "4":
                self.gracz.wyswietl_statystyki()
            elif choose == "5":
                print("Do zobaczenia!")
                break        
            elif choose == "6":
                self.gracz.zapisz_stan("stan_gry.txt")
            elif choose == "7":
                self.gracz.wczytaj_stan("stan_gry.txt")
        
        
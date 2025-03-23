from Statystyki import Statystyki
from Lokalizacje import Lokalizacje

class Menu:
    def __init__(self):
        self.gracz = Statystyki("Gracza",100, 10, 50)
        self.kowal = Lokalizacje("Kowal", "Stary kowal, ktory ulepsza bron.")
        self.sklep = Lokalizacje("Sklep", "Sklep z przedmiotami.")
        self.karczma = Lokalizacje("Karczma", "Karczma, gdzie mozna odpoczac.")
        self.polowanie = Lokalizacje("Polowanie", "Polowanie na potwory.")

    def menu(self):
        while True:
            print("\nWybierz co chcesz zrobic:")
            print("1 - Idz do kowala ulepszyc bron")
            print("2 - Idz do sklepu")
            print("3 - Idz do karczmy odpoczac")
            print("4 - Idz na polowanie")
            print("5 - Zobacz statystyki")
            print("6 - Wyjscie")
            choose = input("Wybierz: ")
            if choose == "1":
                self.kowal.kowal()
            elif choose == "2":
                self.sklep.sklep()
            elif choose == "3":
                self.karczma.karczma()
            elif choose == "4":
                self.polowanie.polowanie()
            elif choose == "5":
                #print(self.gracz)
                self.gracz.gracz()
            elif choose == "6":
                print("Do zobaczenia!")
                break        
        
        
from Statystyki import Statystyki

class Lokalizacje:

    def __init__(self, nazwa, opis, gracz):
        self.nazwa = nazwa  
        self.opis = opis
        self.gracz = gracz  # Tworzymy obiekt gracza jako atrybut klasy
        #Potwory
        # self.potwory=[]
        # self.potwory.append(Statystyki("1 - Goblin", 50, 5, 10))
        # self.potwory.append(Statystyki("2 - Ork",50, 20, 100))
        # self.potwory.append(Statystyki("3 - Golem", 75, 30, 150))
        # self.potwory.append(Statystyki("4 - Smok", 100, 40, 200))
        # self.gracz = Statystyki("Gracza",100, 10, 50)


    def kowal(self):
        print(self.opis)
        print("1. Ulepsz broń - koszt 5G")
        print("2. Wyjdź")
        akcja = input("Wybierz akcję: ") 
        if akcja == "1":
            self.gracz.up_kowal(5, 5)
        elif akcja == "2":
            print("Do widzenia!")
        print ("---------------------------------")

    def karczma(self):
        print(self.opis)
        print("1. Odpocznij")
        print("2. Wyjdź")
        akcja = input("Wybierz akcję: ")
        if akcja == "1":
           self.gracz.up_karczma()
        elif akcja == "2":
            print("Do widzenia!")
        print ("---------------------------------")

    def polowanie(self):
        print(self.opis)
        print("1. Poluj")
        print("2. Wyjdź")
        akcja = input("Wybierz akcję: ")
        if akcja == "1":
            print("Wybierz potwora:")
            print("1. Goblin")
            print("2. Ork")
            print("3. Golem")
            print("4. Smok")
            choose = input("Wybierz potwora: ")
            if choose == "1":
                self.gracz.walka_Goblin(30, 5)
            elif choose == "2":
                self.gracz.walka_Ork(50, 10)
            elif choose == "3":
                self.gracz.walka_Golem(75, 15)
            elif choose == "4":
                self.gracz.walka_Smok(100, 20)
            else:
                print("Nie ma takiego potwora!")
        elif akcja == "2":
            print("Do widzenia!")
        print ("---------------------------------")
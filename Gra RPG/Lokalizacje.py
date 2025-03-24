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
  #          self.gracz.wyswietl_statystyki()
        elif akcja == "2":
            print("Do widzenia!")
        print ("---------------------------------")

    def karczma(self):
        print(self.opis)
        print("1. Odpocznij")
        print("2. Wyjdź")
        akcja = input("Wybierz akcję: ")
        if akcja == "1":
           self.gracz.up_karczma(100)
        elif akcja == "2":
            print("Do widzenia!")
        print ("---------------------------------")

    def polowanie(self):
        print(self.opis)
        print("1. Poluj")
        print("2. Wyjdź")
        akcja = input("Wybierz akcję: ")
        if akcja == "1":
            print("Wybierz potwora z ktorym chcesz walczyc: ")
            for potwor in self.potwory:
                print(potwor)
            wybor = input("Wybierz potwora: ")
            if wybor == "1":
                print("Walczysz z goblinem!")
            elif wybor == "2":
                print("Walczysz z orkiem!")
            elif wybor == "3":
                print("Walczysz z golemem!")
            elif wybor == "4":
                print("Walczysz ze smokiem!")
        elif akcja == "2":
            print("Do widzenia!")
        print ("---------------------------------")
from Statystyki import Statystyki

class Lokalizacje:
    def __init__(self, nazwa, opis):
        self.nazwa = nazwa  
        self.opis = opis
        #Potwory
        self.potwory=[]
        self.potwory.append(Statystyki("1 - Goblin", 50, 5, 10))
        self.potwory.append(Statystyki("2 - Ork",50, 20, 100))
        self.potwory.append(Statystyki("3 - Golem", 75, 30, 150))
        self.potwory.append(Statystyki("4 - Smok", 100, 40, 200))

    def kowal(self):
        print(self.opis)
        print("1. Ulepsz broń")
        print("2. Wyjdź")
        akcja = input("Wybierz akcję: ") 
        if akcja == "1":
            print("Broń ulepszona!")
        elif akcja == "2":
            print("Do widzenia!")
        print ("---------------------------------")

    def sklep(self):
        print(self.opis)
        print("1. Kup przedmiot")
        print("2. Sprzedaj przedmiot")
        print("3. Wyjdź")
        akcja = input("Wybierz akcję: ")
        if akcja == "1":
            print("Przedmiot kupiony!")
        elif akcja == "2":
            print("Przedmiot sprzedany!")
        elif akcja == "3":
            print("Do widzenia!")
        print ("---------------------------------")

    def karczma(self):
        print(self.opis)
        print("1. Odpocznij")
        print("2. Wyjdź")
        akcja = input("Wybierz akcję: ")
        if akcja == "1":
            print("Odpoczynek!")
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
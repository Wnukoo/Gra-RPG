class Lokalizacje:
    def __init__(self, nazwa, opis):
        self.nazwa = nazwa  
        self.opis = opis

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
            print("Polowanie!")
        elif akcja == "2":
            print("Do widzenia!")
        print ("---------------------------------")
class Pracownik:
    def __init__(self, imie, nazwisko, wynagrodzenie):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynagrodzenie = wynagrodzenie

    def pobierz_imie(self):
        return self.imie

    def pobierz_nazwisko(self):
        return self.nazwisko

    def pobierz_wynagrodzenie(self):
        return self.wynagrodzenie


pracownik1 = Pracownik("Konstantyn", "Banaszkiewicz", 5)
pracownik2 = Pracownik("Jully", "Brzęczyszczykiewicz", 6700)

print("Imię:", pracownik1.pobierz_imie())
print("Nazwisko:", pracownik1.pobierz_nazwisko())
print("Wynagrodzenie:", pracownik1.pobierz_wynagrodzenie())

print("Imię:", pracownik2.pobierz_imie())
print("Nazwisko:", pracownik2.pobierz_nazwisko())
print("Wynagrodzenie:", pracownik2.pobierz_wynagrodzenie())

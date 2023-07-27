class Ksiazka:
    def __init__(self):
        self.tytul = None
        self.autor = None
        self.rok_wydania = None

    def dodawanie_tytulu(self, tytul):
        self.tytul = tytul

    def pobieranie_tytulu(self):
        return self.tytul

    def dodawanie_autora(self, autor):
        self.autor = autor

    def pobieranie_autora(self):
        return self.autor

    def dodawanie_roku_wydania(self, rok_wydania):
        self.rok_wydania = rok_wydania

    def pobieranie_roku_wydania(self):
        return self.rok_wydania


ksiazka = Ksiazka()

ksiazka.dodawanie_tytulu("Brzydkie kaczątko")
print("Tytuł książki:", ksiazka.pobieranie_tytulu())

ksiazka.dodawanie_autora("Andersen")
print("Autor:", ksiazka.pobieranie_autora())

# ksiazka.dodawanie_roku_wydania("Nie wiem")
print("Rok wydania:", ksiazka.pobieranie_roku_wydania())

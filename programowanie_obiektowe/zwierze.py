class Zwierze:
    def __init__(self, gatunek):
        self.gatunek = gatunek

    def wydawanie_dzwieku(self, dzwiek):
        return dzwiek

    def pobieranie_info_o_gatunku(self, wielkosc, ubarwienie):
        return wielkosc, ubarwienie


zwierze = Zwierze('Baran')
dzwiek = zwierze.wydawanie_dzwieku('beczenie')
wyglad = zwierze.pobieranie_info_o_gatunku('duży', 'bialy i brudny')
print('Gatunek:', zwierze.gatunek)
print('Dźwięk:', dzwiek)
print('Wygląd:', wyglad)

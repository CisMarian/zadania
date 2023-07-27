class Wydarzenie:
    def __init__(self, nazwa_wydarzenia):
        self.nazwa_wydarzenia = nazwa_wydarzenia
        self.data = None
        self.opis = None
        self.miejsce = None

    def ustawianie_daty(self, data):
        self.data = data

    def pobieranie_daty(self):
        return self.data

    def ustawianie_opisu(self, opis):
        self.opis = opis

    def pobieranie_opisu(self):
        return self.opis

    def ustawianie_miejsca(self, miejsce):
        self.miejsce = miejsce

    def pobieranie_miejsca(self):
        return self.miejsce


wydarzenie1 = Wydarzenie("Piąte urodziny chorej córki")
wydarzenie1.ustawianie_daty("6 lipca 2027 r.")
wydarzenie1.ustawianie_opisu(
    "Mam chorą córkę, proszę o darmowe prezenty i koce dla orek"
    )
wydarzenie1.ustawianie_miejsca("Majorka")

print(wydarzenie1.nazwa_wydarzenia)
print("Data:", wydarzenie1.pobieranie_daty())
print("Opis:", wydarzenie1.pobieranie_opisu())
print("Miejsce:", wydarzenie1.pobieranie_miejsca())

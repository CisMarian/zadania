import math


class Punkt:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def ustaw_x_y(self, x, y):
        self.x = x
        self.y = y

    def pobierz_x_y(self):
        return (self.x, self.y)

    def oblicz_odleglosci_miedzy_punktami(self, punkt):
        odleglosc = math.dist((self.x, self.y), (punkt.x, punkt.y))

        return odleglosc


punkt1 = Punkt()
punkt1.ustaw_x_y(4, 18)
print('Współrzędne punktu', punkt1.pobierz_x_y())

punkt2 = Punkt()
punkt2.ustaw_x_y(1, 6)
print('Współrzędne punktu', punkt2.pobierz_x_y())

odleglosc = punkt1.oblicz_odleglosci_miedzy_punktami(punkt2)
zaokrąglona_odleglosc = round(odleglosc, 2)
print('Odległość między punktami:', zaokrąglona_odleglosc)

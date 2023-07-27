class Prostokat:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def oblicz_pole(self):
        pole_prostokata = self.a * self.b

        return pole_prostokata

    def oblicz_obwod(self):
        obwod_prostokata = 2 * self.a + 2 * self.b

        return obwod_prostokata


prostokat = Prostokat(2, 3)

pole = prostokat.oblicz_pole()
print("Pole prostokata: ", pole)

obwod = prostokat.oblicz_obwod()
print("Obwód prostokąta: ", obwod)

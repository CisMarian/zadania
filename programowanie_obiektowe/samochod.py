class Samochod:
    def __init__(self):
        self.predkosc = 0

    def przyspieszanie(self):
        if self.predkosc < 140:
            self.predkosc += 5
            print("Przyśpieszam, aktualna prędkość", self.predkosc)
        else:
            print("Jedziesz zbyt szybko.")

    def hamowanie(self):
        if self.predkosc > 5:
            self.predkosc -= 5
            print("Hamowanie udane, aktualna prędkość ", self.predkosc)
        else:
            self.predkosc = 0
            print("Prędkość jest za mała, aby móc hamować,Ty prawie stoisz")

    def aktualna_predkosc(self):
        print("Prędkość samochodu:", self.predkosc)


samochod = Samochod()
samochod.przyspieszanie()
samochod.hamowanie()
samochod.aktualna_predkosc()

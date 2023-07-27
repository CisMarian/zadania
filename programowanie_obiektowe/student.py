class Student:
    def __init__(self, imie, nazwisko, srednia):
        self.imie = imie
        self.nazwisko = nazwisko
        self.srednia = srednia

    def pobieranie_imienia(self):
        return self.imie

    def pobieranie_nazwiska(self):
        return self.nazwisko

    def pobieranie_sredniej(self):
        return self.srednia


student = Student("Jan", "Kazimierczańskibarański", 4.8)

print("Imię:", student.pobieranie_imienia())
print("Nazwisko:", student.pobieranie_nazwiska())
print("Średnia:", student.pobieranie_sredniej())

class KontoBankowe:
    def __init__(self):
        self.stan_konta = 0

    def wplac(self, wplacana_kwota):
        self.stan_konta += wplacana_kwota
        return self.stan_konta

    def wyplac(self, wyplacana_kwota):
        if wyplacana_kwota > self.stan_konta:
            print("Nie masz wystarczających środów na koncie")
        else:
            print("Wypłacanie środków")
            self.stan_konta -= wyplacana_kwota

    def sprawdz_stan_konta(self):
        return self.stan_konta


konto_bankowe = KontoBankowe()

stan_konta = konto_bankowe.sprawdz_stan_konta()
print("Stan konta:", stan_konta)

wplata = konto_bankowe.wplac(580)
print("Wpłacono:", wplata)
stan_konta += wplata
print("Stan konta:", stan_konta)

konto_bankowe.wyplac(1000)
print("Stan konta", stan_konta)

konto_bankowe.wyplac(100)

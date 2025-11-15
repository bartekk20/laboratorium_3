# Zad 4. dodatkowe
# Zamówiłeś w restauracji z grupą x przyjaciół, n potraw (liczbę zamówionych dań i liczbę gości, za
# każdym razem wskazuje użytkownik), następnie dla każdej potrawy podajesz jej cenę.
# Korzystając z pętli while napisz program, który pozwoli obliczyć średnią cenę zamówionej potrawy.
# Podziel sprawiedliwe rachunek miedzy wszystkich gości.

grupa_przyjaciol = int(input("Podaj liczbę przyjaciół: "))
liczba_potraw = int(input("Podaj liczbę potraw: "))

suma_cen = 0
i = 1
while i <= liczba_potraw:
    cena_potrawy = float(input(f"Podaj cenę potrawy {i}: "))
    suma_cen += cena_potrawy
    i += 1

srednia_cena = suma_cen / liczba_potraw

rachunek = suma_cen / grupa_przyjaciol

print("Średnia cena potrawy:", round(srednia_cena, 2), "zł")
print("Rachunek do zapłacenia przez każdego przyjaciela:", round(rachunek, 2), "zł")


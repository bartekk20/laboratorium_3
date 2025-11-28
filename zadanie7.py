# zad 7
# a
n = int(input("Podaj liczbę studentów: "))

i = 0
suma = 0

while i < n:
    punkty = int(input(f"Podaj liczbę punktów studenta {i+1}: "))

    if punkty < 0 or punkty > 100:
        print("Błędna wartość! Podaj liczbę z zakresu 0–100.")
        continue   # pomija resztę pętli, nie zwiększa licznika i

    suma += punkty
    i += 1

srednia = suma / n
print("Średnia liczba punktów:", srednia)

# b
suma = 0
licznik = 0

while True:   # pętla nieskończona
    punkty = input("Podaj liczbę punktów (lub wpisz 'koniec' aby zakończyć): ")

    if punkty.lower() == "koniec":
        break

    punkty = int(punkty)

    if punkty < 0 or punkty > 100:
        print("Błędna wartość! Podaj liczbę z zakresu 0–100.")
        continue

    suma += punkty
    licznik += 1

if licznik > 0:
    srednia = suma / licznik
    print("Średnia liczba punktów:", srednia)
else:
    print("Nie podano żadnych poprawnych wyników.")



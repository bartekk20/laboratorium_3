# Mając podana listę ulic w danej dzielnicy i wiedząc, że na każdej ulicy znajduje się 5 bloków
# mieszkalnych, a w każdym z nich jest 10 lokali, wypisz listę wszystkich adresów w dzielnicy.
# Lista ulic w dzielnicy:
# • Jagodowa,
# • Lipowa,
# • Kwiatowa,
# • Kasztanowa,
# • Polna

lista_ulic = ["Jagodowa", "Lipowa", "Kwiatowa", "Kasztanowa", "Polna"]

for lista_ulic in lista_ulic:
    for lista_blokow in range(1, 6):
        for lista_lokali in range(1, 11):
            print("Ulica: ", lista_ulic, lista_blokow, "/", lista_lokali)
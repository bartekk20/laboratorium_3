# Zad. 1
# Napisz program, który będzie kontrolować zużycie paliwa w samolocie. Przed rozpoczęciem każdej
# jednostki czasu wydrukuj do konsoli informację o pozostałych jednostkach paliwa. Gdy paliwo
# zostanie wyczerpane, wydrukuj do konsoli informacje 'Konie lotu.'.
# Masz do dyspozycji następujące dane.:
# • ilość paliwa w samolocie w litrach
# • ilość paliwa zużywanego na sekundę w litrach
# • czas lotu w sekunadach
# Wartości początkowe:
# • paliwo = 100
# • paliwo_zużyte_na_s = 10
# • czas = 0

ilosc_paliwa_w_samolocie_w_litrach = 100
ilosc_paliwa_zuzywanego_na_sekunde_w_litrach = 10
czas_lotu_w_sekundach = 0

print("Posiadasz początkowo:", ilosc_paliwa_w_samolocie_w_litrach, "l paliwa\n", "Zużywasz na sekundę: ", ilosc_paliwa_zuzywanego_na_sekunde_w_litrach, "l paliwa")

while(ilosc_paliwa_w_samolocie_w_litrach >= 0):
    print("Czas: ", czas_lotu_w_sekundach, "s", "Stan paliwa: ", ilosc_paliwa_w_samolocie_w_litrach)
    czas_lotu_w_sekundach += 1
    ilosc_paliwa_w_samolocie_w_litrach = ilosc_paliwa_w_samolocie_w_litrach - ilosc_paliwa_zuzywanego_na_sekunde_w_litrach
print("Koniec lotu.")



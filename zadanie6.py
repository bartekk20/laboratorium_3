# Napisz pętlę nieskończoną, w której użytkownik podaje liczby całkowite. W przypadku liczby ujemnej,
# następuję wyjście z pętli.

liczba_uzytkownika = 0

while(True):
    liczba_uzytkownika = int(input("Podaj liczbe dodatnią (ujemna zakończy program): "))
    if liczba_uzytkownika < 0:
        break
print("Podałeś liczbę ujemną!", "->", liczba_uzytkownika, "<-")

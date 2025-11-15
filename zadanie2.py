# Zad. 2.
# Napisz program, który wydrukuje do konsoli 10 pierwszych liczb pierwszych rozdzielonych
# przecinkiem tak jak pokazano poniżej.
# Pamiętaj, że liczba pierwsza - to taka liczba naturalna, która ma dokładnie dwa dzielniki naturalne:
# jedynkę i samą siebie.
# W rozwiązaniu użyj pętli while oraz instrukcji break
# Oczekiwany wynik
# 2,3,5,7,11,13,17,19,23,29


liczba = 2
liczby_pierwsze = []
while len(liczby_pierwsze) < 10:
    dzielniki = 0
    for i in range(1, liczba + 1):
        if liczba % i == 0:
            dzielniki += 1
    if dzielniki == 2:
        liczby_pierwsze.append(liczba)

    liczba += 1
print(*liczby_pierwsze, sep=',')
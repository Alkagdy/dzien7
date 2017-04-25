plik = open("mojplik.txt")

print("To jest pierwsza linijka:")

print(plik.readline(), end='')  # to end powoduje, ze nie dodaje nowej pustej linijki

tresc = plik.read(16) # podana liczba i tyle znakow przeczyta
print(tresc)

plik.close()


plik = open('mojplik.txt', 'r')

linijka = plik.readline()
print(len(linijka))

#sprawdzam pozycje kursora
print(plik.tell())

linijka = plik.readline()
print(linijka)

plik.close()

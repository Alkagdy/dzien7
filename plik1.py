#otwieramy plik
plik = open("mojplik.txt")

#cala sciezka
#plik = open(~\\PycharmProjects\\dzien7\\mojplik.txt")

linijka = plik.readline()
print(linijka)

plik.close()




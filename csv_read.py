baza = []

with open("osoby.txt") as plik:

#lista kolumn
    opis_kolumn = plik.readline()
    for line in plik:

    #usuwamy whitespace
        line = line.strip()

        osoba = line.split(",")

        baza.append(osoba)
print(baza)

for wpis in baza:
    print(wpis[0])

    





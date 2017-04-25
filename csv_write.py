osoba = ["pamela", "anderson", 50]

#mam str i jednego int
#musze zamienic na str wszystko - patrz nizej

osoba_str = [str(dane) for dane in osoba]

dane_zapis = ",".join(osoba_str)

with open("osoby.txt", 'a') as plik:
    plik.write(dane_zapis + "\n")

#zapisalo pamele w moim pliku osoby.txt
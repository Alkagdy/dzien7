import pickle

dane = ["Bartosz", "Mojo", "23"]

#zapisujemy swoje dane
with open("ogorek.txt", "wb") as plik:
    pickle.dump(dane, plik)

#odczytanie
with open("ogorek.txt", "rb") as plik:
    dane_wczytane = pickle.load(plik)

    print(dane_wczytane)


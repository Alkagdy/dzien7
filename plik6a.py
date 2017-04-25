with open("mojplik.txt", 'r+') as plik:
    zawartosc = plik.read()

    if zawartosc[-1] == '\n':
        plik.write("Dane zapisane do pliku")
    else:
        plik.write("\nDane zapisane do pliku")

#bedzie zaczynal zawsze od nowej lini bo sprawdza ostatni znak. Dodaje nowe zdanie w pliku txt


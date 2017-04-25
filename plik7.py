#lista imion
lista =["Ala", "Ola", "Jola"]

#plik nie istnieje
#otwieramy w trybie w albo a
with open("imiona.txt", 'w') as plik:
    #to pod spodem zapisze elementy jednym ciagiem: AlaOlaJola
    #plik.writelines(lista)

    for element in lista:
        plik.write(element + "\n")

    #to powyzej zapisuje imiona jedno pod drugim


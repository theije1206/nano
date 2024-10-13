from games.raad_het_nummer import test
from games.dagboek_nano import ask_password

def vraag():
    while True:
        print("Menu:")
        print("1: Raad het getal")
        print("2: Dagboek")
        print("-----")

        keuze = int(input("Voer een keuze in tussen 1-2: "))

        if keuze < 1 or keuze > 2:
            print('Dit is niet een geldige invoer')
            continue

        if keuze == 1:
            test()
        elif keuze == 2:
            ask_password()
vraag()

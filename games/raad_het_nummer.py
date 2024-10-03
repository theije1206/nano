import random

def test():
    naam = input('Enter your name: ')
    line = naam + ', welkom bij het nummer-raadspel!'
    print(line)
    print('Je mag 3 keer raden')
    print('Raad een nummer tussen 1 en 10:')
    randomNummer = random.randint(1, 10)

    for poging in range(3):
        gok = int(input('Je gok: '))

        if gok < randomNummer:
            print('Je hebt te laag gegokt')
        elif gok > randomNummer:
            print('Je hebt te hoog gegokt')
        else:
            print('Gefeliciteerd, je hebt het nummer geraden!')
            break
    else:
        print('Helaas, je hebt het nummer niet geraden. Het nummer was ' + str(randomNummer))
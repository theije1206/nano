def datum_vrij(datum_input):
    infile = open("../datum.txt", "r")
    bezette_datums = [line.strip() for line in infile.readlines()]
    infile.close()

    if datum_input in bezette_datums:
        return False  # Datum is bezet
    else:
        return True  # Datum is vrij

def ask_password():
    # Herhaal totdat het juiste wachtwoord is ingevoerd
    while True:
        wachtwoord = input("Voer het wachtwoord in: ")

        if wachtwoord == "Geheim1234":
            break
        else:
            print("Het ingevoerde wachtwoord is fout, probeer opnieuw.")

    datum = input('Welkom, om welke datum gaat het (DD-MM-YYYY)? ')

    # Controleer of de datum nog vrij is
    if datum_vrij(datum):
        print(f"De datum {datum} is nog vrij.")
    else:
        # Vraag of de gebruiker tekst wil herschrijven
        toevoegen_herschrijven = input(f"De datum {datum} is al bezet, wilt u tekst herschrijven? (ja/nee): ")

        if toevoegen_herschrijven == "ja":
            nieuwe_tekst = input("Wat wilt u herschrijven? ")
            print(f"Uw nieuwe tekst is: {nieuwe_tekst}")

        elif toevoegen_herschrijven == "nee":
            print("Er is geen tekst herschreven.")
import json

def datum_vrij(datum_input):
    with open("datum.json", "r") as infile:
        bezette_datums = json.load(infile)

    # Controleer of de datum aanwezig is in het JSON-bestand
    return datum_input not in bezette_datums

def voeg_datum_toe(datum_input, nieuwe_tekst):
    with open("datum.json", "r") as infile:
        bezette_datums = json.load(infile)

    # Voeg de nieuwe tekst toe voor de opgegeven datum
    bezette_datums[datum_input] = nieuwe_tekst

    with open("datum.json", "w") as outfile:
        json.dump(bezette_datums, outfile, indent=4)

def herschrijf_datum(datum_input, nieuwe_tekst):
    with open("datum.json", "r") as infile:
        bezette_datums = json.load(infile)

    # Herschrijf de tekst voor de opgegeven datum
    bezette_datums[datum_input] = nieuwe_tekst

    with open("datum.json", "w") as outfile:
        json.dump(bezette_datums, outfile, indent=4)

def ask_password():
    # Herhaal totdat het juiste wachtwoord is ingevoerd
    while True:
        wachtwoord = input("Voer het wachtwoord in: ")

        if wachtwoord == "Geheim1234":
            print("Wachtwoord is correct.")
            break
        else:
            print("Het ingevoerde wachtwoord is fout, probeer opnieuw.")

    # Start het menu voor het invoeren van een datum
    while True:
        datum = input('Welkom, om welke datum gaat het (DD-MM-YYYY)? ')

        # Controleer of de datum nog vrij is
        if datum_vrij(datum):
            print(f"De datum {datum} is nog vrij, wilt u tekst toevoegen? (ja/nee)")
            toevoegen = input().lower()

            if toevoegen == "ja":
                nieuwe_tekst = input("Voer de tekst in die u wilt toevoegen: ")
                voeg_datum_toe(datum, nieuwe_tekst)
                print(f"De tekst '{nieuwe_tekst}' is toegevoegd aan de datum {datum}.")
            else:
                print("Er is geen tekst toegevoegd.")
            break

        else:
            # Vraag of de gebruiker tekst wilt herschrijven
            toevoegen_herschrijven = input(f"De datum {datum} is al bezet, wilt u tekst herschrijven? (ja/nee): ")

            if toevoegen_herschrijven == "ja":
                herschrijven = input("Wat wilt u herschrijven? ")
                herschrijf_datum(datum, herschrijven)
                print(f"Uw nieuwe tekst is: {herschrijven}")
            elif toevoegen_herschrijven == "nee":
                print("Er is geen tekst herschreven.")
            break

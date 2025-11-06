#Uppgift:1 sten, sax, påse
program_namn = "Python312"
print("Nu ska vi spela sten, sax eller påse!")
print(f"Jag är {program_namn}")
spelar_namn = input("Ange ditt namn -> ")
spelar_poäng = 0
program_poäng = 0
import random as nacho
while True:
    try:
        omgångar = int(input("ange antal omgångar som vi ska spela ->"))
        break
    except ValueError:
        print("NNNNAAAAAEEEEJJJJ")
for runda in range(1, omgångar + 1):
    vinnare = "UNKNOWN"
    print(f"Spelomgång {runda}")
    program_drag = nacho.choice(["sten", "sax", "påse"])

    while True:
        val = input("Välj 'Sten', 'Sax' eller 'Påse'-> ")
        if val.lower() in ["sax", "sten", "påse"]:
            break
        else:
            pass

    if program_drag == "sten" and val == "sten":
        vinnare == "Oavgjort"
    elif program_drag == "sax" and val == "sax":
        vinnare == "Oavgjort"
    elif program_drag == "påse" and val == "påse":
        vinnare == "Oavgjort"
    elif program_drag == "sax" and val == "påse":
        program_poäng += 1
        vinnare == program_namn
    elif program_drag == "påse" and val == "sax":
        spelar_poäng += 1
        vinnare == spelar_namn
    elif program_drag == "sten" and val == "påse":
        spelar_poäng += 1
        vinnare == spelar_namn
    elif program_drag == "påse" and val == "sten":
        program_poäng += 1
        vinnare == program_namn
    elif program_drag == "sax" and val == "sten":
        spelar_poäng += 1
        vinnare == spelar_namn
    elif program_drag == "sten" and val == "sax":
        program_poäng += 1
        vinnare == program_namn

    print(f"{spelar_namn} spelar: {val}\n{program_namn} spelar: {program_drag}\n\nVinnare i spelomgång {runda}: {vinnare}!")
print(f"\nSLUTRESULTAT\n{14 * "="}\n{program_namn}: {program_poäng}P\n{spelar_namn}: {spelar_poäng}P\n")

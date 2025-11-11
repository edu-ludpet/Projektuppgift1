#Uppgift:1 sten, sax, påse
#vinnare = "UNKNOWN"
#program_namn = "Python312"
#print("Nu ska vi spela sten, sax eller påse!")
#print(f"Jag är {program_namn}")
#spelar_namn = input("Ange ditt namn -> ")
#spelar_poäng = 0
#program_poäng = 0

#import random as nacho
#while True:
#    try:
#        omgångar = int(input("ange antal omgångar som vi ska spela ->"))
#        break
#    except ValueError:
#        pass
#for runda in range(1, omgångar + 1):
#    print(f"Spelomgång {runda}\n---------------")
#    program_drag = nacho.choice(["sten", "sax", "påse"])

#    while True:
#        val = input("Välj 'Sten', 'Sax' eller 'Påse'-> ")
#        if val.lower() in ["sax", "sten", "påse"]:
#            break
#        else:
#            pass

#    if program_drag == "sten" and val == "sten":
#        vinnare = "Oavgjort"
#    elif program_drag == "sax" and val == "sax":
#        vinnare = "Oavgjort"
#    elif program_drag == "påse" and val == "påse":
#        vinnare = "Oavgjort"
#    elif program_drag == "sax" and val == "påse":
#        program_poäng += 1
#        vinnare = program_namn
#    elif program_drag == "påse" and val == "sax":
#        spelar_poäng += 1
#        vinnare = spelar_namn
#    elif program_drag == "sten" and val == "påse":
#        spelar_poäng += 1
#        vinnare = spelar_namn
#    elif program_drag == "påse" and val == "sten":
#        program_poäng += 1
#        vinnare = program_namn
#    elif program_drag == "sax" and val == "sten":
#        spelar_poäng += 1
#        vinnare = spelar_namn
#    elif program_drag == "sten" and val == "sax":
#        program_poäng += 1
#        vinnare = program_namn
#    if program_poäng > spelar_poäng:
#        spel_vinnare = program_namn
#    else:
#        spel_vinnare = spelar_namn

#    print(f"{spelar_namn} spelar: {val}\n{program_namn} spelar: {program_drag}\n\nVinnare i spelomgång {runda}: {vinnare}!")
#print(f"\nSLUTRESULTAT\n{14 * "="}\n{program_namn}: {program_poäng}P\n{spelar_namn}: {spelar_poäng}P\n")
#print(f"Vinnare: {spel_vinnare}")


#uppgift 2: ordgissningspel
#antal_bokstäver =
#print("Du ska gissa ett ord, bokstav för bokstav, på {antal_bokstäver} bokstäver")
#gissa = input("Ange en gissning->")
#ord_lst = ["is", "sol", "bok", "fågel", "blomma", "skola", "resväska", "fotbollslag", "bibliotekarie", "kärleksförklaring"]

#uppgift 3: Mastermind
print("Datorn kommer slumpa fram en kod på fyra siffror mellan 1 och 6.")
print("Du ska försöka gissa denna kods siffror på max 12 drag.")
print("Efter respektive gissning så kommer du att få en respons:")
print("För varje gissad korrekt siffra på korrekt plats i koden: ✔")
print("För varje gissad korrekt siffra på fel plats i koden: []")
print("För de siffror som inte finns med i koden ges ingen markering.")
print("\nExempel: om den slumpade koden är 2315\noch du gissar 3165\nså blir responsen ✔[][]")
print("\nDu får välja mellan två svårighetsnivåer:")
print("Lättare nivå: Alla siffror är garanterat olika")
print("Svårare nivå: Det kan finnas upprepningar av en eller flera siffror")
nivå = int(input("\nAnge önskad nivå: lättare (1), svårare (2) ->"))
if nivå == 1:
    print("loser")
elif nivå == 2:
    print("tuff")
else:
    print("Calling indian tech support (not a scam)")

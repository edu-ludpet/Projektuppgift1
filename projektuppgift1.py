#Uppgift:1 sten, sax, påse
vinnare = "UNKNOWN"
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
        pass
for runda in range(1, omgångar + 1):
    print(f"Spelomgång {runda}\n---------------")
    program_drag = nacho.choice(["sten", "sax", "påse"])

    while True:
        val = input("Välj 'Sten', 'Sax' eller 'Påse'-> ")
        if val.lower() in ["sax", "sten", "påse"]:
            break
        else:
            pass

    if program_drag == "sten" and val == "sten":
        vinnare = "Oavgjort"
    elif program_drag == "sax" and val == "sax":
        vinnare = "Oavgjort"
    elif program_drag == "påse" and val == "påse":
        vinnare = "Oavgjort"
    elif program_drag == "sax" and val == "påse":
        program_poäng += 1
        vinnare = program_namn
    elif program_drag == "påse" and val == "sax":
        spelar_poäng += 1
        vinnare = spelar_namn
    elif program_drag == "sten" and val == "påse":
        spelar_poäng += 1
        vinnare = spelar_namn
    elif program_drag == "påse" and val == "sten":
        program_poäng += 1
        vinnare = program_namn
    elif program_drag == "sax" and val == "sten":
        spelar_poäng += 1
        vinnare = spelar_namn
    elif program_drag == "sten" and val == "sax":
        program_poäng += 1
        vinnare = program_namn
    if program_poäng > spelar_poäng:
        spel_vinnare = program_namn
    else:
        spel_vinnare = spelar_namn

    print(f"{spelar_namn} spelar: {val}\n{program_namn} spelar: {program_drag}\n\nVinnare i spelomgång {runda}: {vinnare}!")
print(f"\nSLUTRESULTAT\n{14 * "="}\n{program_namn}: {program_poäng}P\n{spelar_namn}: {spelar_poäng}P\n")
print(f"Vinnare: {spel_vinnare}")


#Uppgift:2 ordgissningspel
ord_lst = ["is", "sol", "bok", "fågel", "blomma", "skola", "resväska", "fotbollslag", "bibliotekarie", "kärleksförklaring"] #lista av ord
import random as nacho
while True:
    random_word = nacho.choice(ord_lst)
    random_word_list = list(random_word)
    antal_gissningar = 10
    antal_bokstäver = len(random_word)
    bokstäver_felgissade = []
    gömda_ordet = "*" * len(random_word)
    print(f"Du ska gissa ett ord, bokstav för bokstav, på {antal_bokstäver} bokstäver")
    while True:
        while True:
            gissning = input("Ange en gissning -> ") #random bokstav från spelare
            if len(gissning) == 1 and gissning.isalpha(): #and gissning != bokstäver_felgissade, #prevents user from typing more then 1 letters and only letters
                gömda_ordet_list = list(gömda_ordet)
                #print(random_word_list) #this is the random_word seperated
                if gissning in random_word:
                    print("Rätt gissning!")
                    for i in range(len(random_word)):
                        if random_word[i] == gissning:
                            gömda_ordet_list[i] = gissning
                    gömda_ordet = "".join(gömda_ordet_list)
                elif gissning in bokstäver_felgissade:
                    pass
                else:
                    bokstäver_felgissade.append(gissning)
                    antal_gissningar -= 1
                print(f"Du har nu {antal_gissningar} st. felgissningar kvar")
                print(f"Felgissningar: {"".join(bokstäver_felgissade)}")
                print("".join(gömda_ordet_list))
                break
            else:
                pass
        if gömda_ordet == random_word:
            break
        elif antal_gissningar <= 0:
            break

    if random_word == gömda_ordet:
        print("Du överlevde!")
    else:
        print(f"Du förlorade :-(\nDet korrekta ordet var: {random_word}")
        while True:
            answer = "x"
            answer = input("Vill du spela en till omgång (j/n) -> ").lower()
            if answer.lower() == "n":
                print("programet stängs")
                break
            elif answer.lower() == "j":
                break
            else:
                pass
        if answer.lower() == "n":
            break
print("utanför loop")




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
print("Svårare nivå: Det kan finnas upprepningar av en eller flera siffror\n")

while True:
    random_digits = 0000
    gissning = "x"
    import random as rand
    while True:
        nivå = input("Ange önskad nivå: lättare (1), svårare (2) ->")
        felgissnings_list = ["","","","","","","","","","","","",]
        if nivå in ("1", "2"):
            break
        else:
            pass
    if nivå == "1": #temporary
        random_digits = rand.sample(["1", "2", "3", "4", "5", "6"], 4)
        code = "".join(random_digits)
        print(code)

    else: #nivå == "2": #temporary
        random_digits = "".join(str(rand.randint(1, 6)) for _ in range(4))
        code = random_digits
        print(code)
    print(nivå)
    # place for both programs
    for runda in range(1, 12 + 1):
        while True:
            gissning = input("Ange gissning som följd av fyra siffror->") # add a cap on number 789
            if len(gissning) != 4 or not gissning.isdigit() or gissning in felgissnings_list:
                pass
            else:
                break

        felgissnings_list[runda -1] = gissning
        print(f"{'Drag #':>12}{'Drag':>10}{'Feedback':>18}\n{'-' * 50}") # could be function since its just visual
        for nacho in range(1, 12 + 1):
            feedback = "?"
            backwards_list = (f"{(13 - nacho):>9}")
            print(backwards_list,end=" ")
            print(f"{felgissnings_list[nacho - 1]:>13}", end=" ")
            print(f"{feedback:>9}")


        print(felgissnings_list)
        #rätt_gissat = sum(gissning[i] == code[i] for i in range (4))

        if gissning == code:
            print("correct")
        print(gissning)
        print(code)


    while True:
        answer = "x"
        answer = input("Vill du spela en till omgång (j/n) -> ").lower()
        if answer.lower() == "n":
            print("programet stängs")
            break
        elif answer.lower() == "j":
            break
        else:
            pass
    if answer.lower() == "n":
        break





def printError():
    print("Sorry, dat snap ik niet...")


def vraagOmNummer(completeVraag):
    while True:
        try:
            nummer = int(input(completeVraag+"\n"))
            return nummer
        except:
            printError()    


def vraagOmTekst(completeVraag, keuzes):
    while True:
        try:
            woord = input(completeVraag+"\n")
            if woord in keuzes:
                return woord
        except: 
            printError()


bakje = False
bolletjesAantal = 0


print("Welkom bij Papi Gelato")
while True:

    #stap 1
    while True:
        bolletjesAantal = vraagOmNummer("Hoeveel bolletjes wilt u?")
        if bolletjesAantal <= 0:
            printError()
        elif bolletjesAantal <= 3:
            bakje = False
            break
        elif bolletjesAantal <= 8:
            bakje = True
            print("Dan krijgt u van mij een bakje met",str(bolletjesAantal),"bolletjes")
            break
        else:
            print("Sorry, zulke grote bakken hebben we niet")


    smaken = bolletjesAantal
    #stap 1.5
    while smaken > 0:
        smaken -= 1
        vraagOmTekst("Welke smaak wilt u voor bolletje nummer "+str(bolletjesAantal-smaken)+"? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?", ["A","C","M","V"])
        

    #stap 2
    if bakje != True:
        antwoord = vraagOmTekst(("Wilt u deze "+str(bolletjesAantal)+" bolletje(s) in A) een hoorntje of B) een bakje?"), ["A", "B"])
        if antwoord == "B":
            bakje = True

    #stap 3 
    houder = ("hoorntje", "bakje")[bakje]
    antwoord = vraagOmTekst(("Hier is uw "+houder+" met "+str(bolletjesAantal)+" bolletje(s). Wilt u nog iets bestellen? (Y/N)"), ["Y","N"])

    if antwoord == "N":
        input("Bedankt en tot ziens!")
        quit()

   
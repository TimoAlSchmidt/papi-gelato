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
bolletjesTotaal = 0
bolletjesAantal = 0
bolletjesPrijs = 1.10
horrentjesAantal = 0
horrentjesPrijs = 1.25
bakjesAantal = 0
bakjesPrijs = 0.75


print("Welkom bij Papi Gelato")
while True:

    #stap 1
    while True:
        bolletjesAantal = vraagOmNummer("Hoeveel bolletjes wilt u?")
        if bolletjesAantal <= 0:
            printError()
        elif bolletjesAantal <= 3:
            break
        elif bolletjesAantal <= 8:
            bakje = True
            bakjesAantal += 1
            print("Dan krijgt u van mij een bakje met",str(bolletjesAantal),"bolletjes")
            break
        else:
            print("Sorry, zulke grote bakken hebben we niet")

    bolletjesTotaal += bolletjesAantal
    smaken = bolletjesAantal
    #stap 1.5
    while smaken > 0:
        smaken -= 1
        vraagOmTekst("Welke smaak wilt u voor bolletje nummer "+str(bolletjesAantal-smaken)+"? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?", ["A","C","M","V"])
        

    #stap 2
    if bakje != True:
        antwoord = vraagOmTekst(("Wilt u deze "+str(bolletjesAantal)+" bolletje(s) in A) een hoorntje of B) een bakje?"), ["A", "B"])
        if antwoord == "B":
            bakjesAantal += 1
            bakje = True
        else:
            horrentjesAantal += 1
            bakje = False

    #stap 3 
    houder = ("hoorntje", "bakje")[bakje]
    antwoord = vraagOmTekst(("Hier is uw "+houder+" met "+str(bolletjesAantal)+" bolletje(s). Wilt u nog iets bestellen? (Y/N)"), ["Y","N"])

    bakje = False
    if antwoord == "N":
        bolletjesTotaalPrijs = round(bolletjesTotaal * bolletjesPrijs, 2)
        horrentjesTotaalPrijs = round(horrentjesAantal * horrentjesPrijs, 2)
        bakjesTotaalPrijs = round(bakjesAantal * bakjesPrijs, 2)
        print("------[\"Papi Gelato\"]------\n")
        if bolletjesAantal > 0:
            print("Bolletjes    "+str(bolletjesTotaal)+" x €"+str(bolletjesPrijs)+"  = €"+str(bolletjesTotaalPrijs))
        
        if horrentjesAantal > 0:
            print("Horrentjes    "+str(horrentjesAantal)+" x €"+str(horrentjesPrijs)+"  = €"+str(horrentjesTotaalPrijs))
        
        if bakjesAantal > 0:
            print("Bakjes    "+str(bakjesAantal)+" x €"+str(bakjesPrijs)+"  = €"+str(bakjesTotaalPrijs))


        input("Bedankt en tot ziens!")
        quit()

   
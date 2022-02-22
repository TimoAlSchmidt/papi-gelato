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
toppingTotaalPrijs = 0
toppingPrijzen = (0.50, 0.30, 0.60, 0.90)



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

    #stap 2.5
    antwoord = vraagOmTekst("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?", ["A", "B", "C", "D"])
    nummer = ord(antwoord)-66
    if nummer >= 0:
        toppingTotaalPrijs += toppingPrijzen[nummer]
        if nummer == 2 and bakje:
            toppingTotaalPrijs += 0.30 #voeg 30 toe als bakje wordt gebruikt



    #stap 3 
    houder = ("hoorntje", "bakje")[bakje]
    antwoord = vraagOmTekst(("Hier is uw "+houder+" met "+str(bolletjesAantal)+" bolletje(s). Wilt u nog iets bestellen? (Y/N)"), ["Y","N"])

    bakje = False
    if antwoord == "N":
        bolletjesTotaalPrijs = round(bolletjesTotaal * bolletjesPrijs, 2)
        horrentjesTotaalPrijs = round(horrentjesAantal * horrentjesPrijs, 2)
        bakjesTotaalPrijs = round(bakjesAantal * bakjesPrijs, 2)
        toppingTotaalPrijs = round(toppingTotaalPrijs, 2)
        print("------[\"Papi Gelato\"]------\n")
        if bolletjesTotaal > 0:
            print("Bolletjes    "+str(bolletjesTotaal)+" x €"+str(bolletjesPrijs)+"  = €"+str(bolletjesTotaalPrijs))
        
        if horrentjesAantal > 0:
            print("Horrentjes    "+str(horrentjesAantal)+" x €"+str(horrentjesPrijs)+"  = €"+str(horrentjesTotaalPrijs))
        
        if bakjesAantal > 0:
            print("Bakjes    "+str(bakjesAantal)+" x €"+str(bakjesPrijs)+"  = €"+str(bakjesTotaalPrijs))

        if toppingTotaalPrijs > 0:
            print("topping      1 x €"+str(toppingTotaalPrijs)+"  = €"+str(toppingTotaalPrijs))


        input("Bedankt en tot ziens!")
        quit()

   
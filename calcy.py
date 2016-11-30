#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 11:51:55 2016

@author: markus
@version: 0.1.1

"""


from math import sqrt

calcy_menu = 1 #Variable, used for branching in the menu

#Reads two floats and return their values
def get2floats ():
    float1 = float(input("Bitte Zahl 1 eingeben: "))
    print("Es wurde "+str(float1)+" eingegeben!\n")
    float2 = float(input("Bitte Zahl 2 eingeben: "))
    print("Es wurde "+str(float2)+" eingegeben!\n")
    return float1, float2

#Adds two variables of any kind, including strings
def add (a, b):
    return a+b

#Subtrakt two variables of any kind except strings
def sub (a, b):
    return a-b

#Multiple two variables
def mult (a, b):
    return a*b

#Divide two variables, catch 0 division
def div (a, b):
    if b==0:
        print("Division durch 0 nicht möglich!")
        return "Division durch 0"
    return a/b

#Powers a with b
def power (a, b):
    return a**b

#Quadratic solution
def quadrat ():
#Read values
    a = float(input("Bitte einen Wert für a eingeben (Darf nicht 0 sein!): "))
    b = float(input("Bitte einen Wert für b eingeben: "))
    c = float(input("Bitte einen Wert für c eingeben: "))

    print("\nEs wurden eingebenen: a="+str(a)+", b="+str(b)+" und c="+str(c)+"!")

#calculate discriminante and handle the value

    discriminante = power(b, 2)-4*a*c
    print("Die Diskriminante ist: "+str(discriminante))
    determinante = sqrt(discriminante)

    if discriminante<0: #Discriminante negativ
        return("Die Diskriminante ist negativ - es kann keine reele Lösung berechnet werden!"), (None)

    if discriminante>0: #Discriminante positiv
        print("Die Diskriminante ist positiv - es sind zwei reele Lösungen vorhanden:\n")
        ergebnis1 = div((-b+determinante), (2*a))
        ergebnis2 = div((-b-determinante), (2*a))
        return ergebnis1, ergebnis2

    if discriminante==0: #Discriminante null
        print("Die Diskriminante ist 0 - es ist eine reele Lösung vorhanden:\n")
        return (div(-b, (2*a))), (None)

def reihe_quadrat (): #calculate quadratic series
    entwicklungspunkt = int(input("Bitte den Entwicklungspunkt eingeben: "))
    intervallende = int(input("Bitte das Intervallende eingeben: "))
    ergebnis = []

    for i in range(entwicklungspunkt, intervallende+1):
        ergebnis.append(i**2)
        
    print("Das Ergbnis ist: ")
    print(ergebnis)
    return ergebnis
    
def reihe_fibonacci (): #calculate Fibonacci series
    entwicklungspunkt = int(input("Bitte den Entwicklungspunkt eingeben: "))
    intervallende = int(input("Bitte das Intervallende eingeben: "))
    
    if entwicklungspunkt<1: #Entwicklungspunkt have to be positiv
        print("Es wurde eine Entwicklungspunkt unter 1 eingegeben!")
        print("Der Entwicklungspunkt wird auf 1 gesetzt!")
        entwicklungspunkt = 1
        
    if intervallende<2: # Intervallende have to be a minimum of 2
        print("Es wurde ein zu kleines Intervallende eingegeben!")
        print("Das Intervallende wurde auf 2 gesetzt!")
        intervallende = 2
        
    if entwicklungspunkt>intervallende: #Entwicklungspunkt have to be in the Intervall
        print("Der Entwicklungspunkt liegt nach dem Intervallende!")
        print("Die Punkte werden daher vertauscht!")
        changer = intervallende
        intervallende = entwicklungspunkt
        entwicklungspunkt = changer
       
#    if entwicklungspunkt==1:
#        nextpoint=2
#
#    while nexpoint<=intervallende:
        
    
    
def reihe_summe (ergebnis): #calculates the sum of serie
    summe = 0
    for i in range(0, len(ergebnis)):
        summe = summe+ergebnis[i]
    print("Die Summe der Reihe ist: "+str(summe))


while calcy_menu>0: #Loop of the menu

    print("\n\nWillkommen bei Calcy!\n")
    print("Bitte waehlen Sie eine Rechenoperation aus dem Menü:\n")
    print("----------Menue----------")
    print("Addition - 1")
    print("Subtraktion - 2")
    print("Multiplikation - 3")
    print("Division - 4")
    print("Potenz - 5")
    print("Quadratische Loesung - 6")
    print("Caro Funktion - 7")
    print("Reihe entwickeln - 8")

    # Quit Calcy
    print("Beenden - 0")

    calcy_menu = int(input("Bitte eine Eingabe taetigen: "))
    print ("Sie haben "+str(calcy_menu)+" gewählt!\n\n")

    if calcy_menu==1: #Addition
        a, b = get2floats()
        print("Das Ergebnis der Addition ist: "+str(add(a, b)))

    elif calcy_menu==2: #Subraction
        a, b = get2floats()
        print("Das Ergebnis der Subtraktion ist: "+str(sub(a, b)))

    elif calcy_menu==3: #Multiplication
        a, b = get2floats()
        print("Das Ergebnis der Multiplikation ist: "+str(mult(a, b)))

    elif calcy_menu==4: #Divison
        a, b = get2floats()
        print("Das Ergebnis ist der Division ist: "+str(div(a, b)))

    elif calcy_menu==5: #Power
        a, b = get2floats()
        print("Das Ergebnis der Potenzfunktion ist: "+str(power(a, b)))

    elif calcy_menu==6: #Quadratic Soloution
        a, b = quadrat()
        if (b==None):
            print(a)
        else:
            print(a)
            print(b)

    elif calcy_menu==7: #Caro
        print("Ich liebe Dich Caro!\nDein Markus")

    elif calcy_menu==8: #Calculate series
        print("-----Reihe entwickeln-----")
        print("Quadratische Reihe - 1")
        print("Fibonacci Reihe - 2")

        #Quit submenu
        print("Beenden des Reihenmenüs - 0")

        calcy_menu = int(input("Bitte eine Eingabe tätigen: "))
        print ("Sie haben "+str(calcy_menu)+" gewählt!\n\n")

        if calcy_menu==1: #Quadratic serie
            print("Sie haben die Entwicklung der quadratischen Reihe gewählt!")
            ergebnis=reihe_quadrat()
            
            print("Wollen Sie die Summe der Reihe berechnen? Ja (1) Nein (2)")
            calcy_menu = int(input("Bitte eine Eingabe tätigen: "))
            
            if calcy_menu==1:
                reihe_summe(ergebnis)
            elif calcy_menu==2:
                print("Die Summe der Reihe wird nicht berechnet.")
            else:
                print("Es wurde keine gültige Auswahl getroffen!")
        
        if calcy_menu==2:
            print("Sie haben die Entwicklung der Fibonacci Reihe gewählt!")
            
        
        
        else: #No valid choice in the submenu
            print("Es wurde keine gültige Auswahl getroffen!")

    else: #No valid choice in the menu
        if calcy_menu!=0:
            print("Es wurde keine gültige Auswahl getroffen!")



        
        
        

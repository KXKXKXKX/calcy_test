#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 11:51:55 2016

@author: markus
@version: 0.1

"""


from math import sqrt

calcy_menu = 1 #Menüschleifenvariable

# Liest zwei Floats ein und liefert diese zurück
def get2floats():
    float1 = float(input("Bitte Zahl 1 eingeben: "))
    print("Es wurde "+str(float1)+" eingegeben!\n")
    float2 = float(input("Bitte Zahl 2 eingeben: "))
    print("Es wurde "+str(float2)+" eingegeben!\n")
    return float1, float2

# Addiert zwei beliebige Typen und liefert als Ergebnis deren Wert (auch mit Strings möglich)
def add (a, b):
    return a+b

#Subtrahiert zwei beliebige Typen (nicht mit Strings möglich)
def sub (a, b):
    return a-b

#Multipliziert zwei Typen
def mult (a, b):
    return a*b

#Dividiert zwei Typen, fängt 0 Division ab
def div (a, b):
    if b==0:
        print("Division durch 0 nicht möglich!")
        return "Division durch 0"
    return a/b

#Liefert a hoch b
def power (a, b):
    return a**b

#Quadratische Lösung
def quadrat ():
#Werte einlesen
    a=float(input("Bitte einen Wert für a eingeben (Darf nicht 0 sein!): "))
    b=float(input("Bitte einen Wert für b eingeben: "))
    c=float(input("Bitte einen Wert für c eingeben: "))

    print("\nEs wurden eingebenen: a="+str(a)+", b="+str(b)+" und c="+str(c)+"!")

#discriminante ermitteln und behandeln

    discriminante=power(b, 2)-4*a*c
    print("Die Diskriminante ist: "+str(discriminante))
    determinante=sqrt(discriminante)

    if discriminante<0: #Discriminante negativ
        return("Die Diskriminante ist negativ - es kann keine reele Lösung berechnet werden!"), (None)

    if discriminante>0: #Discriminante positiv
        print("Die Diskriminante ist positiv - es sind zwei reele Lösungen vorhanden:\n")
        ergebnis1 = div((-b+determinante), (2*a))
        ergebnis2 = div((-b-determinante), (2*a))
        return ergebnis1, ergebnis2

    if discriminante==0: #Discriminante Null
        print("Die Diskriminante ist 0 - es ist eine reele Lösung vorhanden:\n")
        return (div(-b, (2*a))), (None)

def reihe_quadrat (): #Quadratische Reihe entwickeln
    entwicklungspunkt=int(input("Bitte den Entwicklungspunkt eingeben: "))
    intervallende=int(input("Bitte das Intervallende eingeben: "))
    ergebnis=[]

    for i in range(entwicklungspunkt, intervallende+1):
        ergebnis.append(i**2)
        
    print("Das Ergbnis ist: ")
    print(ergebnis)
    return ergebnis
    
def reihe_fibonacci (): #Fibonacci Reihe entwicklen
    entwicklungspunkt=int(input("Bitte den Entwicklungspunkt eingeben: "))
    intervallende=int(input("Bitte das Intervallende eingeben: "))
    
    if entwicklungspunkt<1: #Entwicklungspunkt muss positiv sein
        print("Es wurde eine Entwicklungspunkt unter 1 eingegeben!")
        print("Der Entwicklungspunkt wird auf 1 gesetzt!")
        entwicklungspunkt=1
        
    if intervallende<2: # Intervallende muss mindestens 2 sein
        print("Es wurde ein zu kleines Intervallende eingegeben!")
        print("Das Intervallende wurde auf 2 gesetzt!")
        intervallende=2
        
    if entwicklungspunkt>intervallende: #Entwicklungspunkt muss im Intervall liegen
        print("Der Entwicklungspunkt liegt nach dem Intervallende!")
        print("Die Punkte werden daher vertauscht!")
        changer=intervallende
        intervallende=entwicklungspunkt
        entwicklungspunkt=changer
       
#    if entwicklungspunkt==1:
#        nextpoint=2
#
#    while nexpoint<=intervallende:
        
    
    
def reihe_summe (ergebnis):
    summe=0
    for i in range(0, len(ergebnis)):
        summe=summe+ergebnis[i]
    print("Die Summe der Reihe ist: "+str(summe))


while calcy_menu>0: #Menüschleife

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

    # Beenden des Taschenrechners
    print("Beenden - 0")

    calcy_menu=int(input("Bitte eine Eingabe taetigen: "))
    print ("Sie haben "+str(calcy_menu)+" gewählt!\n\n")

    if calcy_menu==1: #Addition
        a, b = get2floats()
        print("Das Ergebnis der Addition ist: "+str(add(a, b)))

    elif calcy_menu==2: #Subraktion
        a, b = get2floats()
        print("Das Ergebnis der Subtraktion ist: "+str(sub(a, b)))

    elif calcy_menu==3: #Multiplikation
        a, b = get2floats()
        print("Das Ergebnis der Multiplikation ist: "+str(mult(a, b)))

    elif calcy_menu==4: #Divison
        a, b = get2floats()
        print("Das Ergebnis ist der Division ist: "+str(div(a, b)))

    elif calcy_menu==5: #Potenz
        a, b = get2floats()
        print("Das Ergebnis der Potenzfunktion ist: "+str(power(a, b)))

    elif calcy_menu==6: #Quadratische Lösungsformel
        a, b = quadrat()
        if (b==None):
            print(a)
        else:
            print(a)
            print(b)

    elif calcy_menu==7: #Caro
        print("Ich liebe Dich Caro!\nDein Markus")

    elif calcy_menu==8: #Reihe entwickeln
        print("-----Reihe entwickeln-----")
        print("Quadratische Reihe - 1")
        print("Fibonacci Reihe - 2")

        #Beenden des Untermenüs
        print("Beenden des Reihenmenüs - 0")

        calcy_menu=int(input("Bitte eine Eingabe tätigen: "))
        print ("Sie haben "+str(calcy_menu)+" gewählt!\n\n")

        if calcy_menu==1: # Quadratische Reihe
            print("Sie haben die Entwicklung der quadratischen Reihe gewählt!")
            ergebnis=reihe_quadrat()
            
            print("Wollen Sie die Summe der Reihe berechnen? Ja (1) Nein (2)")
            calcy_menu=int(input("Bitte eine Eingabe tätigen: "))
            
            if calcy_menu==1:
                reihe_summe(ergebnis)
            elif calcy_menu==2:
                print("Die Summe der Reihe wird nicht berechnet.")
            else:
                print("Es wurde keine gültige Auswahl getroffen!")
        
        if calcy_menu==2:
            print("Sie haben die Entwicklung der Fibonacci Reihe gewählt!")
            
        
        
        else: #Keine gültige Auswahl im Menü getroffen
            print("Es wurde keine gültige Auswahl getroffen!")

    else: #Keine gültige Auswahl im Menü getroffen
        if calcy_menu!=0:
            print("Es wurde keine gültige Auswahl getroffen!")



        
        
        

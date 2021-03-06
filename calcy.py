#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
First Version created on Mon Nov 28 11:51:55 2016

@author: m, m@arkus.at
@version: 0.1.8.1

A mighty calculator for different problems, Testcoding for getting practice with GIT
Markus Spreitzer, 09.01.2017
"""


from math import sqrt
#import numpy as np
import matplotlib.pyplot as plt


def main ():


    calcy_menu = 1 #Variable, used for branching in the menu
    
    
    def get2floats (): #Reads two floats and return their values
    
        float1 = float(input("Bitte Zahl 1 eingeben: "))
        print("Es wurde "+str(float1)+" eingegeben!\n")
        float2 = float(input("Bitte Zahl 2 eingeben: "))
        print("Es wurde "+str(float2)+" eingegeben!\n")
        return float1, float2
    
    
    def add (a, b): #Adds two variables of any kind, including strings
        return a+b
    
    
    def sub (a, b): #Subtract two variables of any kind except strings
        return a-b
    
    
    def mult (a, b): #Multiple two variables
        return a*b
    
    
    def div (a, b): #Divide two variables, catch 0 division
    
        if b==0:
            print("Division durch 0 nicht möglich!")
            return "Division durch 0"
        return a/b
    
    
    def power (a, b): #Powers a with b
         return a**b
    
    
    def factorial_logic (): #logic for caluclating the factorial of an integer
        
        value = -1
        while value<0:
            value = int(input("Bitte die Zahl eigeben von welcher die Fakultät berechnet werden soll: "))
            if value<0:
                print("Die Zahl muss größer oder gleich 0 sein!")
                print("Bitte erneut eine Zahl eingeben!")
                
        return factorial(value)
        
        
    def factorial (a): #calculate the factorial of an integer recursiv
        
        if a==0:
            return 1
        else:
            return factorial(a-1)*a
         
         
         
    def quadrat (): #Quadratic solution
        
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
     
        
    def reihe_fibonacci_logic (): #handles Fibonacci series logic
    
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
        
        #starting condition
        firstpoint = 1
        nextpoint = 2
            
        reference = reihe_fibonacci_calc(firstpoint, nextpoint, intervallende) #calculate the reference serie till the intervallende
    
        i = 0
        while reference[i]<entwicklungspunkt: #find start in the reference
            i += 1
                
        reference = reference [i::]
        return reference
    
       
    def reihe_fibonacci_calc (first, second, end): #calculate the fibonacci serie, need a valid start (first, second)
    
        ergebnis = []
        ergebnis.append(first)
        i = 0
        newelement = second
        
        while newelement<=end: #check if the end is reached, if then break the loop
            ergebnis.append(newelement)
            newelement = ergebnis[i] + ergebnis[i+1]
            i += 1
        
        return ergebnis
        
            
    def reihe_summe (ergebnis): #calculates the sum of serie
        
        print("Wollen Sie die Summe der Reihe berechnen? Ja (1) Nein (2)")
        menu = int(input("Bitte eine Eingabe tätigen: "))
        
        if menu==1:
            summe = 0
            for i in range(0, len(ergebnis)):
                summe = summe+ergebnis[i]
            print("Die Summe der Reihe ist: "+str(summe))
            
        elif menu==2:
            print("Die Summe der Reihe wird nicht berechnet.")
            
        else:
            print("Es wurde keine gültige Auswahl getroffen! Die Summe wird daher nicht berechnet!")
            
    
    def reihe_colatz_problem ():
        
        value = -1 #start value
        ergebnis = []
        while value<=0:
            value = int(input("Bitte die Zahl eigeben von welcher das Colatz Problem entwickelt werden soll: "))
            if value<=0:
                print("Die Zahl muss größer 0 sein!")
                print("Bitte erneut eine Zahl eingeben!")
                
        maxvalues = 0 #how many values will be calculated
        while maxvalues<=0:
            maxvalues = int(input("Wie viele Werte sollen berechnet werden? (Achtung! Nicht mehr als 1000 empfohlen!)\n"))
            if maxvalues<=0:
                print("Die Zahl muss größer 0 sein!")
                print("Bitte erneut eine Zahl eingeben!")
                
        for i in range(0, maxvalues):
            ergebnis.append(value)
                    
            if (value%2)==0: #even
                value//=2
            else: #odd
                value = value*3+1
                
            #check if konvergent
            
            if value==1:
                if ergebnis[len(ergebnis)-1]==2:
                    if ergebnis[len(ergebnis)-2]==4:
                        ergebnis.append(value)
                        break
                        
                        
        print("\nEs wurden "+str(len(ergebnis))+" Werte berechnet:")
        if len(ergebnis)==maxvalues:
            print("Achtung es wurde nach Erreichen von "+str(maxvalues)+" Werten abgebrochen!")
        
        return ergebnis
        
        
    def reihe_prime (enable=0, value=-1):
        
        ergebnis = []
        
        #add definition of prime
        
        ergebnis.append(1)
        
        counter = 3
        
        if enable==0: #if enable is 0, normal mode -> prime series, if not -> prime tester mode
        
            value = -1 #start value, bigger than 1
            while value<=0:
                value = int(input("Bitte die Zahl eingeben bis zu welcher Primzahlen entwickelt werden sollen: "))
                if value<=0:
                    print("Die Zahl muss größer 0 sein!")
                    print("Bitte erneut eine Zahl eingeben!")
            
            
        if value==1:
            return ergebnis
        else:
            ergebnis.append(2)
            
        trigger = 0
            
        while (value>=ergebnis[len(ergebnis)-1]): #first loop, breaks if the primes runs out of range
            
            for i in ergebnis: #second loop breaks, if prime is found
                
                if((counter%i==0) and not (i is ergebnis[0])):
                    trigger = 1 #shortcut if not prime, it breaks at first division with remainer 0
                    break
                
            if (trigger == 0): #prime is found, writing to array
                ergebnis.append(counter)
            else:
                trigger = 0
            counter += 1
        
        ergebnis.pop() #removes last element to be in range, it has to develop one element more than requested to make sure that the previous was the last one
            
        return ergebnis
        
    def reihe_prime_tester ():
        
        value = -1 #start value, bigger than 1
        while value<=0:
            value = int(input("Bitte die Zahl eingeben welche getestet werden soll: "))
            if value<=0:
                print("Die Zahl muss größer 0 sein!")
                print("Bitte erneut eine Zahl eingeben!")
                
        if value == 1:
            print("1 ist eine Primzahl per Definition!")
            return True
            
        else:
            primes = []
            primes = reihe_prime(1, value)
            for i in primes:
                if (i==value):
                    print(str(value)+" ist eine Primzahl!")
                    return True
            print(str(value)+" ist KEINE Primzahl!")
            return False
        
    def print_graph (title, reihe):
        
        print("Wollen Sie die Reihe plotten? Ja (1) Nein (2)")
        menu = int(input("Bitte eine Eingabe tätigen: "))
        
        if menu==1:
            print("Achtung die Skalierung wird logarithmisch dargestellt!")
            plt.title(title)
            plt.plot(reihe, "r+-")
            plt.xlabel("X-Achse")
            plt.ylabel("Y-Achse")
            plt.show()
            
        elif menu==2:
            print("Die Reihe wird nicht geplottet.")
            
        else:
            print("Es wurde keine gültige Auswahl getroffen! Die Reihe wird daher nicht geplottet!")
        
    
    while calcy_menu>0: #Loop of the menu
    
        print("\n\nWillkommen bei Calcy!\n")
        print("Bitte waehlen Sie eine Rechenoperation aus dem Menü:\n")
        print("----------Menü----------")
        print("Addition - 1")
        print("Subtraktion - 2")
        print("Multiplikation - 3")
        print("Division - 4")
        print("Potenz - 5")
        print("Quadratische Loesung - 6")
        print("Fakultät - 7")
        print("Reihe entwickeln - 8")
    
        # Quit Calcy
        print("Beenden - 0")
        
    
        calcy_menu = int(input("Bitte eine Eingabe tätigen: "))
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
    
        elif calcy_menu==7: #Factorial
            ergebnis = factorial_logic()
            print("Das Ergebnis ist: ")
            print(ergebnis)
            
    
        elif calcy_menu==8: #Calculate series
            print("-----Reihe entwickeln-----")
            print("Quadratische Reihe - 1")
            print("Fibonacci Reihe - 2")
            print("Colatz Problem - 3")
            print("Primzahlenreihe entwickeln - 4")
            print("Einzelne Zahl auf Primzahl untersuchen - 5")
    
            #Quit submenu
            print("Beenden des Reihenmenüs - 0")
    
            calcy_menu = int(input("Bitte eine Eingabe tätigen: "))
            print ("Sie haben "+str(calcy_menu)+" gewählt!\n\n")
    
            if calcy_menu==1: #Quadratic serie
                print("Sie haben die Entwicklung der quadratischen Reihe gewählt!")
                ergebnis = reihe_quadrat()
                print("Die quadratische Reihe ist: ")
                print(ergebnis)
                reihe_summe(ergebnis)
                print_graph("Quadratische Reihe", ergebnis)
            
            elif calcy_menu==2: #fibonacci series
                print("Sie haben die Entwicklung der Fibonacci Reihe gewählt!")
                ergebnis = reihe_fibonacci_logic()
                print("Die Fibonacci Reihe ist: ")
                print(ergebnis)
                reihe_summe(ergebnis)
                print_graph("Fibonacci Reihe", ergebnis)
                
            elif calcy_menu==3: #callatz series
                print("Sie haben das Colatz Problem gewählt!")
                ergebnis = reihe_colatz_problem()
                print(ergebnis)
                reihe_summe(ergebnis)
                print_graph("Colatz Werte", ergebnis)
                
            elif calcy_menu==4: #prime series
                print("Sie haben die Primzahlenreihe gewählt!")
                ergebnis = reihe_prime()
                print(ergebnis)
                reihe_summe(ergebnis)
                print_graph("Primzahlen", ergebnis)
                
            elif calcy_menu==5: #prime tester
                print("Sie haben den Primzahltester gewählt!")
                reihe_prime_tester()
            
            elif calcy_menu==0: #return to the main menu
                print("Rückkehr zum Hauptmenü...")
                calcy_menu = 8
            
            else: #No valid choice in the submenu
                print("Es wurde keine gültige Auswahl getroffen!")
                calcy_menu = 8 #reset back to the series value
                
        elif calcy_menu==9: #testing
            print("Test")
    
        #edit
    
        else: #No valid choice in the menu
            if calcy_menu!=0:
                print("Es wurde keine gültige Auswahl getroffen!")
    
    
    
    exit(1) #terminate programm
    


if __name__ == "__main__":
    main();
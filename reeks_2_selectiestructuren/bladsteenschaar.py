keuze1 = input()
keuze2 = input()
winnaar = -1

if keuze1 == "schaar":
    if keuze2 == "blad" or keuze2 == "hagedis":
      winnaar = 1
    if keuze2 == "Spock" or keuze2 == "steen":
       winnaar = 2
if keuze1 == "blad":
   if keuze2 == "steen" or keuze2 == "Spock":
      winnaar = 1
   if keuze2 == "hagedis" or keuze2 == "schaar":
      winnaar = 2
if keuze1 == "steen":
   if keuze2 == "schaar" or keuze2 == "hagedis":
      winnaar = 1
   if keuze2 == "blad" or keuze2 == "Spock":
      winnaar = 2
if keuze1 == "hagedis":
   if keuze2 == "Spock" or keuze2 == "blad":
      winnaar = 1
   if keuze2 == "steen" or keuze2 == "schaar":
      winnaar = 2
if keuze1 == "Spock":
   if keuze2 == "schaar" or keuze2 == "steen":
      winnaar = 1
   if keuze2 == "hagedis" or keuze2 == "blad":
      winnaar = 2

if winnaar != -1:
   print(f"speler{winnaar} wint")
else:
   print("gelijkspel")

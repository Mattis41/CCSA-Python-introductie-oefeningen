g1 = int(input())
g2 = int(input())
g3 = int(input())
g4 = int(input())
g5 = int(input())
g6 = int(input())
g7 = int(input())
g8 = int(input())
g9 = int(input())
controler = int(input()) 

# Vermenigvuldig elk getal met zijn positie in de reeks
totaal = (1*g1 + 2*g2 + 3*g3 + 4*g4 + 5*g5 + 6*g6 + 7*g7 + 8*g8 + 9*g9)

if totaal % 11 == controler:
    print("OK")
else:
    print("FOUT")
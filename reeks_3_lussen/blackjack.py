getal = 1
som = 0
while getal != 0 and som < 21:
    getal = int(input())
    som+=getal

if som < 21:
    print(f"Voorzichtig gespeeld ({som})")
if som == 21:
    print("Gewonnen!")
if som > 21:
    print(f"Verbrand ({som})")

    
getal1 = int(input())
getal2 = int(input())
def bevriend(getal):
    sum = 0
    for i in range (1,getal):
        if(getal%i == 0):
            sum+=i
    return sum

print(f"{getal1} en {getal2} zijn{"" if bevriend(getal1) == getal2 and bevriend(getal2) == getal1 else " geen"} bevriende getallen")
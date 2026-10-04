eerste_weging = input()
tweede_weging = input()
getal = -1
if eerste_weging == "links":
    if tweede_weging == "links":
        getal = 5
    if tweede_weging == "rechts":
        getal = 4
    if tweede_weging == "evenwicht":
        getal = 6
if eerste_weging == "rechts":
    if tweede_weging == "links":
        getal = 2
    if tweede_weging == "rechts":
        getal = 1
    if tweede_weging == "evenwicht":
        getal = 3
if eerste_weging == "evenwicht":
    if tweede_weging == "links":
        getal = 8
    if tweede_weging == "rechts":
        getal = 7
    if tweede_weging == "evenwicht":
        getal = 9
print(f"muntstuk #{getal} is vervalst")

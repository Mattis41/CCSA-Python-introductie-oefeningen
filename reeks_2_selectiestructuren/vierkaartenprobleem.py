w = input()    
getal = input()
draai = input()
if w == "waarde":
    getal = int(getal)
    if(getal%2 == 0):
        if draai == "nee":
            print(f"Fout: kaarten met waarde {getal} moeten gedraaid worden.")
        else:
            print(f"Juist: kaarten met waarde {getal} moeten gedraaid worden.")
    else:
        if draai =="nee":
            print(f"Juist: kaarten met waarde {getal} moeten niet gedraaid worden.")
        else:
            print(f"Fout: kaarten met waarde {getal} moeten niet gedraaid worden.")

else:
    if(getal == "rood"):
        if draai == "nee":
            print(f"Juist: kaarten met kleur {getal} moeten niet gedraaid worden.")
        else:
            print(f"Fout: kaarten met kleur {getal} moeten niet gedraaid worden.")
    else:
        if draai == "nee":
            print(f"Fout: kaarten met kleur {getal} moeten gedraaid worden.")
        else:
            print(f"Juist: kaarten met kleur {getal} moeten gedraaid worden.")

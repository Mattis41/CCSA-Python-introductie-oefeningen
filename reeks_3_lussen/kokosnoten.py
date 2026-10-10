# piraten = int(input())
# noten = int(input())

# for i in range(piraten):
#     notenpiraat = noten // piraten
#     notenErvoor = noten
#     noten = noten - notenpiraat - 1

#     print(f"{notenErvoor} {"noten" if notenErvoor == 1 else "noot" } = {notenpiraat} {"noten" if notenErvoor == 1 else "noot" } voor piraat#{i+1} en 1 noot voor de aap")

# print(f"elke piraat krijgt {(noten - noten%piraten )// piraten} {"noot" if (noten - noten%piraten )// piraten  == 1 else "noten" } en {noten%piraten} {"noot" if noten%piraten == 1 else "noten" } voor de aap")

piraten = int(input())
noten = int(input())

for i in range(piraten):
    notenpiraat = noten // piraten
    notenErvoor = noten
    noten = noten - notenpiraat - 1

    print(f"{notenErvoor} {'noot' if notenErvoor == 1 else 'noten'} = {notenpiraat} {'noot' if notenpiraat == 1 else 'noten'} voor piraat#{i+1} en 1 noot voor de aap")

# Berekeningen voor de overgebleven noten
aantal_per_piraat = noten // piraten  # kortere manier om (noten - noten % piraten) // piraten te schrijven
rest_voor_aap = noten % piraten

print(f"elke piraat krijgt {aantal_per_piraat} {'noot' if aantal_per_piraat == 1 else 'noten'} en {rest_voor_aap} {'noot' if rest_voor_aap == 1 else 'noten'} voor de aap")
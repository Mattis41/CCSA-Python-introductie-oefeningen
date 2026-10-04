h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())

start = h1 * 60 + m1
end = h2 * 60 + m2

if h2 == 0 and m2 == 0:
    end = 24 * 60

if start < 18 * 60 or end > 24 * 60 or end <= start:
    print("ongeldige invoer")
else:

    start_zone1 = max(start, 18 * 60)
    end_zone1 = min(end, 21 * 60 + 30)

    minuten_zone1 = max(0, end_zone1 - start_zone1)


    start_zone2 = max(start, 21 * 60 + 30)
    end_zone2 = min(end, 24 * 60)
    minuten_zone2 = max(0, end_zone2 - start_zone2)


    totaal = (minuten_zone1 / 60) * 2 + (minuten_zone2 / 60) * 4
    
    print(totaal)
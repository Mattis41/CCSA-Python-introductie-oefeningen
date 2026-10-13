def maximale_blootstelling(db):
    if db < 80:
        return -1
    else:
        aantalKeerDelen = (db-80)//3
        tijd = 8*60*60
        gehalveerdeTijd = tijd / (2**aantalKeerDelen)
        return float(gehalveerdeTijd)

db = float(input("geef me decibel"))
print(maximale_blootstelling(db))
def berekenPrijs(aantal):
    prijs = ((24.95) - (24.95 * 40)/100)*aantal + 3 + (aantal-1) * 0.75
    return prijs
print(berekenPrijs(60))
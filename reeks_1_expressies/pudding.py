aantal_stuks = int(input())
kostPrijs = float(input())
aantalBarCodes = int(input())
aantalMijl = int(input())

print(f"Phillips spendeerde ${float(aantal_stuks * kostPrijs)} voor {int(int(aantal_stuks/aantalBarCodes))*aantalMijl} frequent flyer mijlen.")
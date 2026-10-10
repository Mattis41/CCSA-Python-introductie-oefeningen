
som_rood_wit = int(input())
som_wit_blauw = int(input())
operator = input().strip()

for b in range(2, som_wit_blauw):
    w = som_wit_blauw - b
    r = som_rood_wit - w
    

    if w >= 2 and r >= 2:

        if operator == '<' and (b + r) < som_wit_blauw:
            print(b)
            print(w)
            print(r)
            break
        elif operator == '>' and (b + r) > som_wit_blauw:
            print(b)
            print(w)
            print(r)
            break
def bereken_beleefdheid(n):
    oneven_delers = 0
    i = 1
    
    while i * i <= n:
        if n % i == 0:
            
            if i % 2 != 0:
                oneven_delers += 1
            
            
            tweede_deler = n // i
            if tweede_deler != i and tweede_deler % 2 != 0:
                oneven_delers += 1
        i += 1
        

    return oneven_delers - 1


n = int(input())

print(bereken_beleefdheid(n))
appels = int(input())
palletten = appels // (20*35)
rest = appels%700
kisten =rest//20
over = rest % 20
print(palletten)
print(kisten)
print(over)

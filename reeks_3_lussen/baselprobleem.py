import math
def f():
    res = 0
    for i in range(1,101):
        res+= 1*(1/i**2)
    print(res)
    return res

target = math.pi**2 / 6
n = 1
while True:
  diff = abs(f() - target)
  if diff <= 1/100:
    print(n)
    break
  n += 1    


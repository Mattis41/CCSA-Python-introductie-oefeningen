
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

x3 = int(input())
y3 = int(input())
x4 = int(input())
y4 = int(input())

min_x1 = min(x1, x2)
max_x1 = max(x1, x2)
min_y1 = min(y1, y2)
max_y1 = max(y1, y2)

min_x2 = min(x3, x4)
max_x2 = max(x3, x4)
min_y2 = min(y3, y4)
max_y2 = max(y3, y4)


overlap_x = min_x1 < max_x2 and max_x1 > min_x2


overlap_y = min_y1 < max_y2 and max_y1 > min_y2


if overlap_x and overlap_y:
    print("botsing")
else:
    print("geen botsing")
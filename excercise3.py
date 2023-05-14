x1 = int(input("value of x1"))
y1 = int(input("value of y1"))
x2 = int(input("value of x2"))
y2 = int(input("value of y2"))

delta_x = x1 - x2
delta_y = y1 - y2

if delta_x == 0 or delta_y == 0:
    print("YES")
elif delta_x == delta_y:
    print("YES")
else:
    print("NO")
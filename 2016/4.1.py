file = open("punkty.txt", "r")
lines = file.readlines()
a = 200
b = 200
r = 200
count = 0
for line in lines:
    x, y = line.split()
    x = int(x)
    y = int(y)
    if (x - a)**2 + (y - b)**2 == r**2:
        print(x, y)
    elif (x - a)**2 + (y - b)**2 < r**2:
        count += 1
print(count)

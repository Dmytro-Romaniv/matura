file = open("punkty.txt", "r")
lines = file.readlines()

wewnatrz = 0
bokach = 0
zewnatrz = 0

for line in lines:
    x, y = line.split()
    x, y = int(x), int(y)
    if (5000 > x > -5000) and (5000 > y > -5000):
        wewnatrz += 1
    elif (x == 5000 or x == -5000) and (5000 >= y >= -5000):
        bokach += 1
    elif (y == 5000 or y == -5000) and (5000 > x > -5000):
        bokach += 1
    else:
        zewnatrz += 1

print("Wewnątrz kwadratu:", wewnatrz, "\n" +
      "Na bokach kwadratu:", bokach, "\n" +
      "Na zewnątrz kwadratu:", zewnatrz)

import math
maxd = [0]

file = open("punkty.txt", "r")
lines = file.readlines()

for line in lines:
    for line2 in lines:
        x, y = line.split()
        x2, y2 = line2.split()
        x, y, x2, y2 = int(x), int(y), int(x2), int(y2)
        distance = round(math.sqrt((x2-x)**2+(y2-y)**2))
        if distance > int(maxd[0]):
            maxd = [distance, x, y, x2, y2]

print("Najwieksza odleglosc:", maxd[0], ", pomiedzy punktami (",
      maxd[1], ";", maxd[2], ") i (", maxd[3], ";", maxd[4], ")")

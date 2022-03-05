file = open("kody.txt", "r")
result = open("kody1.txt", "w")
lines = file.readlines()

for line in lines:
    sumaP, sumaN = 0, 0
    for i in range(0, len(line.strip())):
        if i % 2 == 0:
            # jest nieparzysta bo 0 = 1 miejsce
            sumaN += int(line[i])
        else:
            sumaP += int(line[i])

    result.write(str(sumaP) + " " + str(sumaN) + "\n")

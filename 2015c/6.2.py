def kontrolna(sp, sn):
    return (10-(3*sp + sn) % 10) % 10


def kod(n):
    if n == 0:
        return 10101110111010
    if n == 1:
        return 11101010101110
    if n == 2:
        return 10111010101110
    if n == 3:
        return 11101110101010
    if n == 4:
        return 10101110101110
    if n == 5:
        return 11101011101010
    if n == 6:
        return 10111011101010
    if n == 7:
        return 10101011101110
    if n == 8:
        return 11101010111010
    if n == 9:
        return 10111010111010


file = open("kody.txt", "r")
result = open("kody2.txt", "w")
lines = file.readlines()

for line in lines:
    sumaP, sumaN = 0, 0
    for i in range(0, len(line.strip())):
        if i % 2 == 0:
            sumaN += int(line[i])
        else:
            sumaP += int(line[i])

    number = kontrolna(sumaP, sumaN)
    result.write(str(number) + " " + str(kod(number)) + "\n")

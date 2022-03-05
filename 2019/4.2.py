def silnia(number):
    fact = 1
    if number == 0 or number == 1:
        return fact
    else:
        for i in range(1, number + 1):
            fact = fact * i
        return fact


file = open("liczby.txt", "r")
lines = file.readlines()
for line in lines:
    suma = 0
    for num in line.strip():
        suma = suma + silnia(int(num))
    if int(line) == suma:
        print(line.strip())

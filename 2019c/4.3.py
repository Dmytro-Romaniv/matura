def waga(n):
    suma = 0
    for item in str(n):
        suma += int(item)
    if suma >= 9:
        return waga(suma)
    return suma


file = open("pierwsze.txt", "r")
lines = file.readlines()
count = 0
for line in lines:
    if waga(int(line)) == 1:
        count += 1
print(count)

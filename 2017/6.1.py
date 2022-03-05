file = open("dane.txt", "r")
lines = file.readlines()
array = []
for line in lines:
    for pixel in line.split():
        array.append(int(pixel))
array.sort()
print("Najmniejsza wartosc: ", array[0])
print("Najwieksza wartosc: ", array[-1])

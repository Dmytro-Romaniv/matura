def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


file = open("NAPIS.txt", "r")
lines = file.readlines()
count = 0

for line in lines:
    suma = 0
    for value in line.strip():
        suma += ord(value)
    if prime(suma):
        count += 1

print(count)

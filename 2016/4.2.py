file = open("punkty.txt", "r")
lines = file.readlines()
a = 200
b = 200
r = 200
nk = 0
n = 0
P = 400**2

for line in lines:
    x, y = line.split()
    x = int(x)
    y = int(y)
    if (x - a)**2 + (y - b)**2 <= r**2:
        nk += 1
    n += 1

pi = (P * nk)/(r ** 2 * n)
print(pi)

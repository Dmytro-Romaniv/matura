file = open("punkty.txt", "r")
lines = file.readlines()

count = 0

for line in lines:
    x, y = line.split()
    if set(x) == set(y):
        count += 1

print(count)
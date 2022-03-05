file = open("liczby.txt", "r")
lines = file.readlines()

count = 0

for line in lines:
    number = line[:-2]
    system = line[-2]
    if int(system) == 8:
        count += 1

print(count)

file = open("liczby.txt", "r")
lines = file.readlines()

count = 0

for line in lines:
    number = line[:-2]
    system = line[-2]
    if int(system) == 4:
        if "0" not in number:
            count += 1

print(count)

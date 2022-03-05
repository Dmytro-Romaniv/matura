file = open("sygnaly.txt", "r")
lines = file.readlines()
maxl = [0, 0]

for line in lines:
    if len(set(line.strip())) > maxl[1]:
        maxl = [line.strip(), len(set(line.strip()))]

print(maxl)

file = open("NAPIS.txt", "r")
lines = file.readlines()
count = 0

for line in lines:
    old = 0
    big = 0
    for value in line.strip():
        if ord(value) > old:
            big += 1
        old = ord(value)
    if big == len(line.strip()):
        print(line.strip())

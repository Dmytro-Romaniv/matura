file = open("NAPIS.txt", "r")
lines = file.readlines()
lines2 = []

for line in lines:
    lines2.append(line.strip())

for line2 in lines2:
    if lines2.count(line2) > 1:
        print(line2)
        lines2.remove(line2)

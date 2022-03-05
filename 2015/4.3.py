file = open("liczby.txt", "r")
lines = file.readlines()
lines2 = []

for line in lines:
    lines2.append(int(line.strip()))
lines2.sort()

print(lines.index(str(lines2[0])+"\n")+1, lines.index(str(lines2[-1])+"\n")+1)

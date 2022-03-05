file = open("dane1.txt", "r")
lines = file.readlines()

file2 = open("dane2.txt", "r")
lines2 = file2.readlines()

count = 0

for i in range(0, len(lines)):

    line = lines[i].split()
    line2 = lines2[i].split()

    if set(line) == set(line2):
        count += 1
        print("Wiersz: ", i+1)

print(count)
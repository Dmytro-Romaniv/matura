file = open("dane1.txt", "r")
lines = file.readlines()

file2 = open("dane2.txt", "r")
lines2 = file2.readlines()

count = 0


for i in range(0, len(lines)):
    line = lines[i].strip().split()
    line2 = lines2[i].strip().split()
    if line[-1] == line2[-1]:
        count += 1

print(count)

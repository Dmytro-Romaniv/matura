file = open("dane1.txt", "r")
lines = file.readlines()

file2 = open("dane2.txt", "r")
lines2 = file2.readlines()

for i in range(0, len(lines)):
    
    group = []
    line = lines[i].split()
    line2 = lines2[i].split()

    for number in line:
        group.append(int(number))
    for number in line2:
        group.append(int(number))

    group.sort()
    print(group)

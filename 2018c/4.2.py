file = open("dane1.txt", "r")
lines = file.readlines()

file2 = open("dane2.txt", "r")
lines2 = file2.readlines()

count = 0

for i in range(0, len(lines)):

    odd_count = 0
    even_count = 0
    odd2_count = 0
    even2_count = 0
    line = lines[i].split()
    line2 = lines2[i].split()

    for number in line:
        if int(number) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    for number in line2:
        if int(number) % 2 == 0:
            even2_count += 1
        else:
            odd2_count += 1

    if even_count == even2_count == 5 and odd_count == odd2_count == 5:
        count += 1

print(count)

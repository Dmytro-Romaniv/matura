file = open("dane.txt", "r")
lines = file.readlines()
count = 0

for line in lines:
    x = line.split()
    for i in range(0, 320):
        if x[i] != x[(-1*i)-1]:
            count += 1
            break

print(count)

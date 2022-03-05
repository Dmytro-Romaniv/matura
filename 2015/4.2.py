file = open("liczby.txt", "r")
lines = file.readlines()

count2 = 0
count8 = 0

for line in lines:
    if line.strip()[-1] == "0":
        count2 += 1
    if line.strip()[-3:] == "000":
        count8 += 1

print(count2, count8)

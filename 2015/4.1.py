file = open("liczby.txt", "r")
lines = file.readlines()
count = 0

for line in lines:
    if line.count("0") > line.count("1"):
        count += 1

print(count)

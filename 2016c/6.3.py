def convert(n, s):
    value = 1
    result = 0
    sys = int(s)
    num = list(n)
    num.reverse()
    for item in num:
        result = result + (int(item)*value)
        value = value * sys
    return result


file = open("liczby.txt", "r")
lines = file.readlines()

count = 0

for line in lines:
    number = line[:-2]
    system = line[-2]
    if int(system) == 2 and convert(number, system) % 2 == 0:
        count += 1

print(count)

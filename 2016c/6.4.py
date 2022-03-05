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
suma = 0

for line in lines:
    number = line[:-2]
    system = line[-2]
    if int(system) == 8:
        suma += convert(number, system)
        
print(suma)

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

tablica = []

for line in lines:
    tablica.append(int(line.strip()))

tablica.sort()
print(tablica[0], convert(str(tablica[0])[:-1], str(tablica[0])[-1]), "\n",
      tablica[-1], convert(str(tablica[-1])[:-1], str(tablica[-1])[-1]))

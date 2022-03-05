from math import gcd

file = open("liczby.txt", "r")
lines = file.readlines()

table = []
max_length = len(table)
prev = max_prev = 1

for line in lines:
    table.append(int(line))
    if gcd(prev, int(line)) == 1:
        table.clear()
    elif len(table) > max_length:
        max_length = len(table)
        max_table = table.copy()
        max_prev = prev
    prev = gcd(*table)

print(max_table[0], len(max_table), max_prev)

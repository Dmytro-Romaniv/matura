file = open("sygnaly.txt", "r")
lines = file.readlines()

i = 39
phrase = ""

while i < len(lines):
    phrase += lines[i][9]
    i += 40

print(phrase)

file = open("pary.txt", "r")
lines = file.readlines()
test = []

for line in lines:
    number, phrase = line.split()
    if int(number) == len(phrase):
        test.append(phrase)
test.sort()
print(len(test[0]), test[0])

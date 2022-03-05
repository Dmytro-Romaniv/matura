def odleglosc(string):
    for letter in string:
        for letter2 in string:
            if abs(ord(letter) - ord(letter2)) > 10:
                return False
    return True


file = open("sygnaly.txt", "r")
lines = file.readlines()

for line in lines:
    if odleglosc(line.strip()):
        print(line.strip())

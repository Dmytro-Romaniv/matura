file = open("pary.txt", "r")
lines = file.readlines()

for line in lines:
    number, phrase = line.split()
    divide, maxf, maxl = "", "", 0
    try:
        for i in range(len(phrase)):
            divide += phrase[i]
            if phrase[i] != phrase[i+1]:
                divide += " "
    except:
        pass
    array = divide.split()
    for item in array:
        if len(item) > maxl:
            maxl = len(item)
            maxf = item
    print(maxf, maxl)

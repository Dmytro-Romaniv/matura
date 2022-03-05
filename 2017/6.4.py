file = open("dane.txt", "r")
lines = file.readlines()
x = []
count = 1
maxi = 0

for line in lines:
    x.append(line.split())

for k in range(0, 320):
    for w in range(0, 200):
        try:
            if int(x[w][k]) == int(x[w+1][k]):
                count += 1
                if count > maxi:
                    maxi = count
            else:
                count = 1
        except:
            count = 1
print(maxi)

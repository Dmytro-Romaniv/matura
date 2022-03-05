file = open("dane.txt", "r")
lines = file.readlines()
x = []
count = 0

for line in lines:
    x.append(line.split())

for w in range(0, 200):
    for k in range(0, 320):
        try:
            if abs(int(x[w][k]) - int(x[abs(w-1)][k])) > 128 or abs(int(x[w][k]) - int(x[w+1][k])) > 128\
               or abs(int(x[w][k]) - int(x[w][abs(k-1)])) > 128 or abs(int(x[w][k]) - int(x[w][k+1])) > 128:
                count += 1
        except:
            pass
            
print(count)

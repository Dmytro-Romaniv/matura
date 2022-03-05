file = open("dane_6_3.txt", "r")
lines = file.readlines()

for line in lines:
    string, new_string = line.split()
    old_key = ord(new_string[0]) - ord(string[0])
    if old_key < 0:
        old_key += 26
    for i in range(len(string)):
        key = ord(new_string[i]) - ord(string[i])
        if key < 0:
            key += 26
        if key != old_key:
            print(string)
            break
        old_key = key

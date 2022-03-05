def cipher(string, key):
    new_string = ""
    string = str(string).strip().upper()
    key = int(key)
    while key > 26:
        key -= 26
    for letter in string:
        if ord(letter) + key > 90:
            new_string += chr(ord(letter) + key - 26)
        else:
            new_string += chr(ord(letter) + key)
    return new_string


file = open("dane_6_1.txt", "r")
lines = file.readlines()

for line in lines:
    print(cipher(line, 107))

def power(number):
    if number == 0:
        return False
    while number != 1:
        if number % 3 != 0:
            return False
        number = number // 3
    return True


count = 0

file = open("liczby.txt", "r")
lines = file.readlines()
for line in lines:
    if power(int(line)):
        count += 1
print(count)
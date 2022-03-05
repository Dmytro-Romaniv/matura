def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


file = open("punkty.txt", "r")
lines = file.readlines()

count = 0

for line in lines:
    x, y = line.split()
    if is_prime(int(x)) and is_prime(int(y)):
        count += 1

print(count)
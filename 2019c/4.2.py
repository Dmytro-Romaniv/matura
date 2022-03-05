def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


file = open("pierwsze.txt", "r")
lines = file.readlines()

for line in lines:
    if prime(int(line.strip()[::-1])):
        print(line.strip())

def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


file = open("liczby.txt", "r")
lines = file.readlines()
for line in lines:
    if 100 <= int(line) <= 5000 and prime(int(line)):
        print(int(line))

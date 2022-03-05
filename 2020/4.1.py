def prime(n):
    if n <= 2:      # only odd
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


file = open("pary.txt", "r")
lines = file.readlines()

for line in lines:
    number, phrase = line.split()
    number = int(number)
    if number % 2 == 0 and number > 4:
        for num in range(number):
            if prime(num) and prime(number - num):
                print(number, num, number - num)
                break
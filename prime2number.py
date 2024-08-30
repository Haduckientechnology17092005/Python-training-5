import math
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print("liet ke ca so nguyen to co 3 chu so: ")
dem = 0
for i in range(100, 1000):
    if isPrime(i):
        print(i, end = " ")
        dem += 1
print("\nco", dem, "so nguyen to")
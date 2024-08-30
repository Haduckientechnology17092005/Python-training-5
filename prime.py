import math
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
print("Tat ca cac so nguyen to nho hon", n, "la: ")
sb = []
if(n>=2):
    sb.append(2)
for i in range(3, n+1, 2):
    if(isPrime(i)):
        sb.append(i)
print(sb)
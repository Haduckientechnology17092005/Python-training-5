import math
def fibonacci(n):
    if n < 0:
        return -1
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True 

n = int(input("Enter a number: "))
print("Tat ca cac so Fibonacci nho hon", n, "la: ")
sb = []
for i in range(0, n):
    if(isPrime(fibonacci(i))):
        sb.append(fibonacci(i))
print(sb)
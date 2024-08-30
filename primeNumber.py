import time
def get_primes(n):
    m = n+1
    numbers = [True]*m
    for i in range(2, int(m**0.5)+1):
        if numbers[i]:
            for j in range(i*i, m, i):
                numbers[j] = False
    primes = []
    for i in range(2, m):
        if numbers[i]:
            primes.append(i)
    return primes

start = time.time()
n = int(input("Enter the number: "))
primes = get_primes(n)
print(primes)
end = time.time()
print("Time taken: ", end - start)
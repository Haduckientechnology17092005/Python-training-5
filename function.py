def luythua():
    a = int(input("Nhập a: "))
    n = int(input("Nhập n: "))
    print("Luỹ thừa của",a,"^",n," là: ", a**n)
    return

luythua()

print("Day fibonaci: ")
def fib(n):
    a,b = 1,1
    while a<=n:
        print(a, end=' ')
        a=b
        b=a+b
    print("\n")
   
fib(10)

def isprime(n):
    if n<2:
        return False
    for i in range (2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

m = int(input("Nhập m: "))
if isprime(m):
    print(m, "là số nguyên tố")
else:
    print(m, "không phải là số nguyên tố")
    
def namnhuan(n):
    if n%4==0 and (n%100!=0 or n%400==0):
        print(n, "là năm nhuận")
    else:
        print(n, "không phải là năm nhuận")

namnhuan(2020)

def ga_tho(dau, chan):
    kl = "Khong co dap so phu hop"
    for i in range (dau+1):
        j = dau - i
        if 2*i + 4*j == chan:
            return i, j, kl
        
dau = 35
chan = 94
dap_an = ga_tho(dau, chan)
print("Dap so la (so ga viet truoc, so tho viet sau): ", dap_an)
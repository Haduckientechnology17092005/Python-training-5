def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
def lcm(a,b):
    return (a*b)//gcd(a,b)

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("UCLN của",a,"và",b,"là: ",gcd(a,b))
print("BCNN của",a,"và",b,"là: ",lcm(a,b))
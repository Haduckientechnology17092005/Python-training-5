import math
def giaiptb2(a,b,c):
    if(a==0):
        if(b==0):
            print("Phuong trinh vo nghiem")
        else:
            print("Phuong trinh co mot nghiem: x= ", -c/b)
        return
    delta = b*b - 4*a*c
    if(delta<0):
        print("Phuong trinh vo nghiem")
    elif(delta==0):
        print("Phuong trinh co mot nghiem kep: x1 = x2 = ", -b/(2*a))
    else:
        print("Phuong trinh co hai nghiem phan biet: ")
        print("x1 = ", (-b + math.sqrt(delta))/(2*a))
        print("x2 = ", (-b - math.sqrt(delta))/(2*a))

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))

giaiptb2(a,b,c)
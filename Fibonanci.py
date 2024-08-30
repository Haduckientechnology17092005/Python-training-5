def fibonanci(n):  
    f0 = 0
    f1 =1
    fn = 1
    if(n<0):
        print("n phai lon hon 0")
        return -1
    elif(n==0 or n==1):
        return n
    else:
        for i in range(2,n+1):
            f0 = f1
            f1 = fn
            fn = f0 + f1
        return fn

print("20 so thuoc day fibonaci la: ")
sb = " "
for i in range(0,20):
    sb = sb + str(fibonanci(i)) + " "
print(sb)
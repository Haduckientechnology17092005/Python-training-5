def uscln(a,b):
    if b==0:
        return a
    else:
        return uscln(b,a%b)
if __name__ == "__main__":
    tu = int(input("Nhập tử số: "))
    mau = int(input("Nhập mẫu số: "))
print("Phan so vua nhap la: ",tu,"/",mau)
print("Phan so toi gian la: ",tu/uscln(tu,mau),"/",mau/uscln(tu,mau))
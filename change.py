def convert_number(n, b):
    if(n<0 or b<2 or b>16):
        return ""
    sb = ""
    m = 0
    remainder = n
    while remainder > 0:
        if b>10:
            m = remainder % b
            if m >= 10:
                sb = sb + str(chr(m+55))
            else:
                sb = sb + str(m)
        else:
            sb = sb + str(remainder % b)
        remainder = remainder // b
    return "".join(reversed(sb))

n = int(input("Nhập n: "))
b = int(input("Nhập b: "))
print("Số",n,"tương đương với",b,"là: ",convert_number(n, b))
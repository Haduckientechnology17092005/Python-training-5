def isSymetric(n):
    str1 = str(n)
    str2 = str1[::-1]
    if str1 == str2:
        return True
    else:
        return False

n = int(input("Enter a number: "))
if isSymetric(n):
    print(n, "is symetric")
else:
    print(n, "is not symetric")
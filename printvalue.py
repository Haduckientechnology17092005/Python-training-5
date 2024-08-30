def inDict():
    print("Dictionary: ")
    d = dict()
    for i in range (2,31):
        d[i] = i**2
    for (k,v) in d.items():
        print(v, end = ' ')
        
inDict()
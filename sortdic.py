List = ["Thuy", "Hoang", "Mai", "Bong", "Nhu", "Kien", "Hang", "Trinh", "Ngoc", "Nguyen"]
def sortList(List):
    ds = List
    for i in range(len(List)-1):
        for j in range(i+1, len(List)):
            if List[i] > List[j]:
                print(List[i], List[j])
                List[i], List[j] = List[j], List[i]
                print(List[i], List[j])
    return List

print(List)
print(sortList(List))
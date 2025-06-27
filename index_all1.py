def index_all(uList,elem):
    result = []
    subpaths = []
    for i,item in enumerate(uList):
        if isinstance(item,list):
            subpaths = index_all(item,elem)
            for path in subpaths:
                result.append([i] + path)
        elif item == elem:
                result.append([i])
    return result

myList = [[[1,2,3],2,[1,3]],2,[1,2,3]]

print(index_all(myList, 2))


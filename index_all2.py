def index_all(uList,elem):
    result = []
    for index,item in enumerate(uList):
        if item == elem:
             result.append([index])
        elif isinstance(uList[index],list):
             for i in index_all(uList[index],elem):
                  result.append([index] + i)
    return result

myList = [[[1,2,3],2,[1,3]],2,[1,2,3]]

print(index_all(myList, 2))
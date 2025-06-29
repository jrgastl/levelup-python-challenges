def index_all(user_list,elem):
    result = []
    for index,item in enumerate(user_list):
        if item == elem:
             result.append([index])
        elif isinstance(user_list[index],list):
             for i in index_all(user_list[index],elem):
                  result.append([index] + i)
    return result

myList = [[[1,2,3],2,[1,3]],2,[1,2,3]]

print(index_all(myList, 2))
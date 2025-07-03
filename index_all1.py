'''
Recursion was the big lesson of this challenge. The most difficult part was to discover how to append the indexes at each run.
'''

def index_all(user_list,elem):
    result = []
    subpaths = []
    for i,item in enumerate(user_list):
        if isinstance(item,list):
            subpaths = index_all(item,elem)
            for path in subpaths:
                result.append([i] + path)
        elif item == elem:
                result.append([i])
    return result

myList = [[[1,2,3],2,[1,3]],2,[1,2,3]]

print(index_all(myList, 2))


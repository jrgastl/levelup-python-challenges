import pickle
def save(py_dict,path):
    with open(path,'wb') as f:
        pickle.dump(py_dict, f)

def load(path):
    with open(path,'rb') as f:
        return pickle.load(f)



# Please, uncomment the lines below to execute the code with the example given

# my_dict = {'a':1,'b':2,'c':3}
# save(my_dict,'./dictionaries/PythonDictionary.pickle')
# recovered = load('./dictionaries/PythonDictionary.pickle')
# print(recovered)
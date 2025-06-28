import json
#Function to take a python dictionary object to file.
def save(pyDict,path):
    with open(path,'w') as f:
        f.write(json.dumps(pyDict))

#Function to load the saved dictionary back to python.
def  load(path):
    with open(path, 'r') as f:
        return json.loads(f.read())

myDict = {'a':1,'b':2,'c':3}

save(myDict,'./dictionaries/PythonDictionary.txt')
recovered = load('./dictionaries/PythonDictionary.txt')
print(recovered)
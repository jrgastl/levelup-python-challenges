'''
Briefing:
Write a python function to build a zip archive.
Input:
    - Directory path
    - List of file extensions
    - Output file path

Output:
    - a ZIP file

ZIP archive should maintain the folder structure

How it should look like:
>>> zip_all('.\\my_stuff',['.jpg','.txt'],'my_stuff.zip')

Documentation source:
https://docs.python.org/3/library/zipfile.html
https://janakiev.com/blog/python-filesystem-analysis/
https://docs.python.org/3/library/pathlib.html
https://peps.python.org/pep-0428/

'''
import zipfile
from pathlib import Path

def zip_all(dir,sufixes,output):

#Look for all the files and retrive the name and the folder path for the ones that have extensions in the extension lists.
    directory = Path(dir)


    
#Create a zip file

#Add the folders and the files to the zip file
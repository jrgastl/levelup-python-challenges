import os
from zipfile import ZipFile

def  zip_all(search_dir, extension_list,  output_path):
    with ZipFile(output_path, 'w') as output_zip:
        for root, _, files in os.walk(search_dir):
            rel_path = os.path.relpath(root, search_dir)
            for file in files:
                _, ext = os.path.splitext(file)
                if ext.lower() in extension_list:
                    output_zip.write(os.path.join(root, file),
                                     arcname=os.path.join(rel_path,file))
                    
# Please, uncomment the line below to execute the code with the example given
# zip_all('./zip',['.txt','.jpg'],'./zip/myfiles.zip')
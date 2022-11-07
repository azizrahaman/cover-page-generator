import os
from glob import iglob
from pdf2jpg import pdf2jpg
import shutil

#root folder that contains subfolder and pdf's
rootdir_glob = 'H:\Python\**\*'
file_list = [f for f in iglob(rootdir_glob, recursive=True) if os.path.isfile(f)]

for f in file_list: 

    check = f.split('.')
    ext = check.pop()
    if ext!='pdf':
        continue

    # remove file name from address to find output location
    split_name = f.split('\\')
    output = split_name[:-1]
    
    #make the first page screenshot
    file_name = split_name.pop()
    inputpath = f
    outputpath = '\\'.join(output)
    result = pdf2jpg.convert_pdf2jpg(inputpath, outputpath, pages="0")
    newLocation = outputpath+"\\"+file_name+"_dir"+"\\"+file_name
    
    #move the file to screenshot folder
    shutil.move(f, newLocation)

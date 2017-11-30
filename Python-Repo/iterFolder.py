import os
import shutil

""" looks over all the files inside photoshop directory and copies them
    in a test folder

    only goes one level deep"""

files = []
rootFolder = 'F:/test/'
for root,directories,filenames in os.walk('F:/Photoshop/'):
    for directory in directories:
        files.append(os.path.join(root,directory))

for x in files:
    subFiles = os.listdir(x)
    for z in subFiles:
        shutil.copy(x+'/'+z,rootFolder)
    #shutil.copytree(x,rootFolder)
        


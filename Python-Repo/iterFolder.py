import os
import shutil

""" looks over all the files inside photoshop directory and copies them
    in a test folder

    only goes one level deep"""

files = []
rootFolder = 'F:/test/'
for root,directories,filenames in os.walk('F:/Photoshop/'):
    for directory in directories:
        x = os.path.join(root,directory)
        subFiles = os.listdir(x)
        for z in subFiles:
            shutil.copy(x+'/'+z,rootFolder)



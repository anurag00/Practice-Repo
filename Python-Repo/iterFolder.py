import os
import shutil

""" looks over all the files inside photoshop directory and copies them
    in a test folder

    only goes one level deep"""

rootFolder = 'F:/test/'
for root,directories,filenames in os.walk('F:/Photoshop/'):
    for directory in directories:
        files = os.path.join(root,directory)
        subFiles = os.listdir(files)
        for z in subFiles:
            shutil.copy(files + '/' + z,rootFolder)

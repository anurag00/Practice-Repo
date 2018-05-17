''' newFile = open()
content = newFile.readlines()
newFile.close()
print(content)
 '''
import os
import locale
print(locale.getdefaultlocale()[1])
#outputs encoding

indexNum = 0
for root, directory, filename in os.walk('G:\\Books'):
    for name in filename:
        if name.endswith('.epub'):
            indexNum += 1
            print(str(indexNum) + ') ' + name)
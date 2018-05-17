import shelve, os

count = 0
shelfFile = shelve.open("G:\\Anurag\\Mydata",)

for dirpath,dirnames,filenames in os.walk('G:\\'):
    for file in filenames:
        if file.endswith('epub'):
            count += 1
            shelfFile[str(count)] = file
            print(count,file)
shelfFile.close()
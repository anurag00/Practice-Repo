import os

def fileFinder(ext,dir):
    count = 0
    for dirpath,dirnames,filenames in os.walk(dir):
        for file in filenames:
            if file.endswith(ext):
                count += 1
                print(count,file," - ",dirpath)

if __name__ == "__main__":
    print("Input the extention to search for => ",end=' ')
    ext = input()
    print("Enter the Directory or path you want to search in =>",end=' ')
    dir = input()
    fileFinder(ext,dir)
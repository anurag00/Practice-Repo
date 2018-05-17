import os, sys

def findWord(word):
    dir = "G:\\Pycode\\Automate"
    for dirpath,dirnames,filenames in os.walk(dir):
        for file in filenames:
            if file.endswith('py'):
                readFile = open(os.path.join(dirpath, file), 'r')
                if word in readFile.read():
                    print(file + ' - ' + dirpath)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = ' '.join(sys.argv[1:])
    else:
        print("Enter word > ",end='')
        word = input()
    findWord(word)
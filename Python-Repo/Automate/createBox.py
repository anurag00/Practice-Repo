"""
*********
*       *
*       *
*       *
*********
"""

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("\'Symbol\' should have a length of 1")
    if (width < 2) or (height < 2):
        raise Exception(r"'Width' and 'Height' must be more than 1")
    print(symbol*width,end='')
    print('')
    for x in range(height-2):
        print(symbol+(' '*(width-2))+symbol)
    print(symbol*width,end='')
    print('')

if __name__ == "__main__":
    '''
    Create a Box with the dimentions entered
    '''
    symbol = input("Symbol = ")
    width = input("width = ")
    height = input("height = ")
    boxPrint(symbol, int(width), int(height))

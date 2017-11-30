import random

def func():
    ''' Checking multiple inequalities
    No arguments passes
    Prints inequality results
    
    Return = None
    '''
    a = random.randint(1,10)
    b = random.randint(1,10)
    c = random.randint(1,10)
    print('For a = {0}, b = {1}, c = {2} a < b < c = {3}'.format(a,b,c,a<b<c))
    print('For a = {0}, b = {1}, c = {2} a < b > c = {3}'.format(a,b,c,a<b>c))
    print('For a = {0}, b = {1}, c = {2} a > b < c = {3}'.format(a,b,c,a>b<c))
    print('For a = {0}, b = {1}, c = {2} a > b > c = {3}'.format(a,b,c,a>b>c),end = '\n\n')

if __name__ == '__main__':
    for x in range(5):
        func()




import math

def checkio(number):

    mul = 1
    
    while number > 10:
        print('{0} {1}'.format(mul,number))
        if number%10 == 0:
            number = int(math.floor(number/10))
            continue
        else:
            mul *= number%10
            number = int(math.floor(number/10))
            print(number)
            
    if number < 10:
        print(mul*number)
        return mul*number
    
    return mul

if __name__ == '__main__':
    checkio(123405)
    checkio(999)
    checkio(1000)
    checkio(1111)

import logging
logging.basicConfig(filename = r'G:\Anurag\MyLogFile.txt',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)

logging.debug('Start of Program')

def factorial(n):
    logging.debug('Start of factorial')
    total = 1
    for x in range(1, n+1):
        total*=x
        logging.info('i is %s, total is %s'%(x,total))

    logging.debug('Return value is %s' %(total))
    return total

print(factorial(5))

logging.debug('End of Program')
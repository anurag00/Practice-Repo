import time, threading

def waitBro():
    print("started 1")
    time.sleep(5)
    print("Awake 1")

def waitBro2():
    threadObj.join()
    print("Started 3")
    time.sleep(5)
    print("Awake 2")

if __name__ == '__main__':
    print("Start of program")

    threadObj = threading.Thread(target = waitBro)
    print(threadObj.getName())
    threadObj.start()

    threadObj3 = threading.Thread(target=waitBro2)
    threadObj3.start()

    threadObj2 = threading.Thread(target=print,args=['cats','dogs','mice'],kwargs={'sep':'&'})
    threadObj2.start()

    print(threading.enumerate())
    print(threading.currentThread())
    print(threading.activeCount())

    print("End of program")
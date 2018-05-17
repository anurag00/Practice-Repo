import subprocess, time, threading

calcProc = subprocess.Popen("calc.exe")
print(calcProc.poll())
calcProc.wait()
time.sleep(1)
print(calcProc.wait())
subprocess.call("notepad.exe")

def printExtra():
    time.sleep(0.5)
    print(threading.currentThread().name,threading.activeCount())

startTime = time.time()

threadobj = []
for x in range(10):
    threadObj1 = threading.Thread(target=printExtra)
    threadObj1.daemon = True
    threadObj1.start()
    threadobj.append(threadObj1)

for x in threadobj:
    x.join()

endTime = time.time()

print("Total time Taken = " + str(endTime - startTime))

subprocess.Popen(['start',r'G:\Anurag\error_log.txt'],shell=True)
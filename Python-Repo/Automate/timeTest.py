import time, datetime

print("tick")
time.sleep(1)
print("Tock")

now = time.time()
print(round(now,2))

#stopwatch
try:
    print("press enter to start and q to stop. Enter for lapping times")
    input()
    startTime = round(time.time(),2)
    lap = 0
    print("started")
    while True:
        x = input()
        if x == 'q':
            raise KeyboardInterrupt
        lap += 1
        lastTime = time.time()
        lapTime = round((lastTime - startTime),2)
        print("Lap " + str(lap) + " Time elapsed = " + str(lapTime))
        startTime = lastTime
except KeyboardInterrupt:
    print('Done...')

#datetime
dt = datetime.datetime.now()
print(dt)
print(dt.day,dt.month,dt.year)
t = time.time()
print(t)
te = datetime.datetime.fromtimestamp(t)
print(te)
print(te.strftime('%A, %d %B %Y'))

delta = datetime.timedelta(days=10, hours=1)
print(delta.days,delta.total_seconds())
print(str(delta))

st = '21st October 2018'
dt2 = datetime.datetime.strptime(st,'%dst %B %Y')
print(dt2)
print((dt2-dt).days)
print(datetime.timedelta(days=(dt2-dt).days))


f = open('links.txt','r')

link = []
for line in f:
    new = line.split(' ')
    print(new[-1])
    link.append(new[-1])
f.close()
f = open('links.txt','w')
f.truncate()
for x in range(len(link)):
    f.write(link[x])
f.close()

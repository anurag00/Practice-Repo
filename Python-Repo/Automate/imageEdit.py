from PIL import Image,ImageColor
import random, subprocess, time, os, signal

#creating custom image with loops

newIm = Image.new('RGBA',(500,500),'green')

'''
#mostly noise
for x in range(2,(newIm.width-2)):
    for y in range(2,(newIm.height-2)):
        randx = random.randint(0,255)
        randy = random.randint(0,255)
        randz = random.randint(0,255)
        newIm.putpixel((x,y),(randx,randy,randz))
'''
# x if cond else y
#refined randomizer
prev = (0,0,0)

#check file
file = open(r'G:\Pycode\Automate\LogRand.txt','w')

incr = 10  # number to incriment and decriment by

for x in range(2,(newIm.width-2)):
    for y in range(2,(newIm.height-2)):
        if prev == (0,0,0):
            randx = random.randint(0,255)
            randy = random.randint(0,255)
            randz = random.randint(0,255)
            newIm.putpixel((x,y),(randx,randy,randz))
            prev = (randx,randy,randz)
        else:
            # more colourful lines
            randnum1 = random.randint(0, 1)
            randnum2 = random.randint(0, 1)
            randnum3 = random.randint(0, 1)
            if randnum1 == 0:
                randx = ((prev[0] - incr) if (prev[0] - incr) > 0 else 0)
            else:
                randx = ((prev[0] + incr) if (prev[0] + incr) < 255 else 255)
            if randnum2 == 0:
                randy = ((prev[1] - incr) if (prev[1] - incr) > 0 else 0)
            else:
                randy = ((prev[1] + incr) if (prev[1] + incr) < 255 else 255)
            if randnum3 == 0:
                randz = ((prev[2] - incr) if (prev[2] - incr) > 0 else 0)
            else:
                randz = ((prev[2] + incr) if (prev[2] + incr) < 255 else 255)

            '''
            #lines
            randnum = random.randint(0,1)
            if randnum == 0:
                randx = ((prev[0] - incr) if (prev[0] - incr) > 0 else 0)
                randy = ((prev[1] - incr) if (prev[1] - incr) > 0 else 0)
                randz = ((prev[2] - incr) if (prev[2] - incr) > 0 else 0)
            else:
                randx = ((prev[0] + incr) if (prev[0] + incr) < 255 else 255)
                randy = ((prev[1] + incr) if (prev[1] + incr) < 255 else 255)
                randz = ((prev[2] + incr) if (prev[2] + incr) < 255 else 255)
            '''

            # randx = random.randint((prev[2] - 10) if (prev[2] - 10) > 0 else 0
            #                        , (prev[2] + 10) if (prev[2] + 10) < 255 else 255)
            newIm.putpixel((x, y), (randx, randy, randz))
            prev = (randx, randy, randz)
            file.write(str(prev)+'\n')


file.close()
newIm.save(r'G:\Pycode\Automate\Randomized.png')
subprocess.Popen(['start',r'G:\Pycode\Automate\Randomized.png'], shell=True)
subprocess.Popen(['start',r'G:\Pycode\Automate\LogRand.txt'], shell=True)
newIm.rotate(90).show()

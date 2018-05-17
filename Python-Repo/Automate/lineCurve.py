from PIL import Image, ImageDraw, ImageFont

size = 300
incr = 10

newIm = Image.new('RGBA',(size,size))
draw = ImageDraw.Draw(newIm)

for i in range(0, size, incr):
    draw.line((i, 0, size, i), fill='white')    # top right

for i in range(0, size, incr):
    draw.line((0, i, i, size), fill='white')    # bottom left

for i in range(0, size, incr):
    draw.line((size - i, 0, 0, i), fill='white')  # top left

for i in range(0, size, incr):
    draw.line((size, i, size - i, size), fill='white')  # bottom right

draw.text((int(size/2-50),(int(size)/2)),"This is the end", fill='white')

newIm.show()
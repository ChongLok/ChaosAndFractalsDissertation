from PIL import Image
Image.MAX_IMAGE_PIXELS = None


im = Image.open('mandelpixelrgb2.png')


black = 0
red = 0

for pixel in im.getdata():
    if pixel == (0, 0, 0):
        black += 1
print('pixels=' + str(black))
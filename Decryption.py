from PIL import Image
img = Image.open("output.png").convert('L')
pixels = list(img.getdata())
for i in pixels:
    print(chr(i),end="")

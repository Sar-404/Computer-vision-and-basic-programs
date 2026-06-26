from PIL import Image
img = Image.open(input("Enter image path in directory\n")).convert('L')
pixels = list(img.getdata())
for i in pixels:
    print(chr(i),end="")

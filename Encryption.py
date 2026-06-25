from PIL import Image
import math
prime_text=False
array=list(input("Enter Text\n"))
for i in range(0,len(array)):array[i]=ord(array[i])
for i in range(2,len(array)):
    if len(array)%i==0:prime_text=True
img = Image.new('L', (math.ceil(math.sqrt(len(array))),math.ceil(math.sqrt(len(array)))))
img.putdata(array)
img.save("output.png")
img.show()

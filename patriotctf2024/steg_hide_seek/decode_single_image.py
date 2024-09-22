from PIL import Image
import pyzbar.pyzbar as pyzbar

img = Image.open('321321321.png')
decoded_objects = pyzbar.decode(img)
if decoded_objects:
    data = decoded_objects[0].data.decode('utf-8')
    print(data)
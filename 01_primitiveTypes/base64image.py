import base64
from PIL import Image
from io import BytesIO

with open("kanye.jpeg", "rb") as image_file:
    data = base64.b64encode(image_file.read())  # this will encode it to a base64 string.

im = Image.open(BytesIO(base64.b64decode(data)))
im.save('newKanye.png', 'PNG')

print(data)

'''
The output of the print(data), the string will be as in the file {encodedImage.txt} (It is a very big string as the image I used is very detailed.)
Please scroll sideways, for the whole string.

'''
# -*- coding: utf-8 -*-
from PIL import Image
import cv2
import os

i=0
while(i==0):
   # read the image file
   imgfile = input('Image file name: ')
   img = cv2.imread(imgfile, 2) 
  
   ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) 

# converting to its binary form 
   bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) 
   try:
      cv2.imwrite("tempimg.jpeg", bw_img) 
   except:
      print("Error reading the image file. try again")
      continue
   i=1
image = Image.open("tempimg.jpeg")
try:
   base_width = int(input('Width: '))
except:
   print('There is an error with the image width')
   base_width = 500
width_percent = (base_width / float(image.size[0]))
hsize = int((float(image.size[1]) * float(width_percent)))
image = image.resize((base_width, hsize))
count = ""
countint=""

numberpix = 127
image.getdata() #returns all the pixels in the image
for pixel in image.getdata():
    if pixel <=numberpix :
        count = count+"1"
        countint = countint+"1"
    else:
        count = count+"0"
        countint = countint+"0"
    if len(countint)%base_width==0:
       count = count+"""
"""
f=open('out.bin', 'w')
f.write(count)
#image.save("ok.jpg")
f.close()
print('You can now find the output in "out.bin" folder.')
if os.path.exists("tempimg.jpeg"):
    os.remove("tempimg.jpeg")
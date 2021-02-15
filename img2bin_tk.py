from tkinter import *
from tkinter import ttk, filedialog
from PIL import Image
import cv2
import os

class imgtobin:

    def __init__(self, master):
        master.configure(bg="#ffffff")
        self.label = ttk.Label(master, text = "Transform an image into a binary file (zeros and ones)!", background='#ffffff')
        self.label.grid(row = 0, column = 0, columnspan = 2)
        ttk.Label(master, text="Resize an image to:", background='#ffffff').grid(row=1, column=0)
        self.entry = Entry(master)
        self.entry.grid(row=1, column=1)
        ttk.Label(master, text="pixels in width", background='#ffffff').grid(row=1, column=2)

        ttk.Button(master, text = "Open image",
                   command = self.select_file).grid(row = 3, column = 0)   

        ttk.Button(master, text = "Transform!",
                   command = self.transform).grid(row = 3, column = 1)    

    def select_file(self):
            self.filename = filedialog.askopenfilename(initialdir="Images", title="Select Image", filetypes=[("Image files", ".jpg .jpeg .png .bmp .gif .jfif")])

    def transform(self):
        i=0
        while(i==0) :
            
            try:
                img = cv2.imread(self.filename, 2)
                ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
                bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
                cv2.imwrite("tempimg.jpeg", bw_img) 
            except:
                self.errimg = ttk.Label(text = "Error reading the image file. try again", background='#ffffff')
                return
            i=1
        image = Image.open("tempimg.jpeg")
        try:
            base_width = int(self.entry.get())
        except:
            base_width = 500
        width_percent = (base_width / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(width_percent)))
        image = image.resize((base_width, hsize))
        count = "Here is your binary image: \n"
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
        f=open('binary.txt', 'w')
        f.write(count)
        #image.save("ok.jpg")
        f.close()
        if os.path.exists("tempimg.jpeg"):
            os.remove("tempimg.jpeg")
        print("Task succeeded!")
        self.openbutton = ttk.Button(text = "Open the final binary file", command = self.open())
    def open(self) :
        os.system("notepad.exe binary.txt")
            


def main():              
    main = Tk()
    app = imgtobin(main)
    main.mainloop()

main()
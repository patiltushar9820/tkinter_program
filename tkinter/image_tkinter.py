#show images using tkinter in python
from tkinter import *
import PIL
from PIL import ImageTk,Image

root=Tk()
root.title('Image Viewer')

my_img1=ImageTk.PhotoImage(Image.open('images/first.png'))
my_img2=ImageTk.PhotoImage(Image.open('images/second.png'))
my_img3=ImageTk.PhotoImage(Image.open('images/third.png'))

image_list=[my_img1,my_img2,my_img3]
my_label=Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

root.mainloop()
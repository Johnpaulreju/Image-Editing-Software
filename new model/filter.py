from tkinter import Label, PhotoImage, Toplevel, Button, RIGHT
import numpy as np
import cv2
from PIL import Image, ImageTk


class FilterFrame(Toplevel):

    def __init__(self, master=None):

        Toplevel.__init__(self, master=master, width="250", height="390")
        saveimg=Image.open(r"Images\bgimg.jpg")
        self.bgimg=ImageTk.PhotoImage(saveimg)

        self.label = Label(master=self,image=self.bgimg)
        self.label.place(x=0, y=0)

        self.original_image = self.master.processed_image
        self.filtered_image = None

        self.negative_button = Button(master=self, text="NEGATIVE",borderwidth=2,fg = 'black',
                 bg = 'yellow',font = (("Times New Roman"),15))
        self.black_white_button = Button(master=self, text="B & W",borderwidth=2,fg = 'black',
                 bg = 'yellow',font = (("Times New Roman"),15))
        self.sepia_button = Button(master=self, text="SEPIA",borderwidth=2,fg = 'black',
                 bg = 'yellow',font = (("Times New Roman"),15))
        self.emboss_button = Button(master=self, text="EMBOSS",borderwidth=2,fg = 'black',
                 bg = 'yellow',font = (("Times New Roman"),15))
        self.gaussian_blur_button = Button(master=self, text="GAUSSIAN BL.",borderwidth=2,fg = 'black',
                 bg = 'yellow',font = (("Times New Roman"),15))
        self.median_blur_button = Button(master=self, text="MEDIAN BLUR",borderwidth=2,fg = 'black',
                 bg = 'yellow',font = (("Times New Roman"),15))
        self.cancel_button = Button(master=self, text="CANCEL",borderwidth=2,fg = 'black',
                 bg = 'yellow',font = (("Times New Roman"),15))
        self.apply_button = Button(master=self, text="APPLY",borderwidth=2,fg = 'black',
                 bg = 'yellow',font = (("Times New Roman"),15))

        self.negative_button.bind("<ButtonRelease>", self.negative_button_released)
        self.black_white_button.bind("<ButtonRelease>", self.black_white_released)
        self.sepia_button.bind("<ButtonRelease>", self.sepia_button_released)
        self.emboss_button.bind("<ButtonRelease>", self.emboss_button_released)
        self.gaussian_blur_button.bind("<ButtonRelease>", self.gaussian_blur_button_released)
        self.median_blur_button.bind("<ButtonRelease>", self.median_blur_button_released)
        self.apply_button.bind("<ButtonRelease>", self.apply_button_released)
        self.cancel_button.bind("<ButtonRelease>", self.cancel_button_released)

        self.negative_button.place(x=60,y=10,width=140,height=30)
        self.black_white_button.place(x=60,y=65,width=140,height=30)
        self.sepia_button.place(x=60,y=120,width=140,height=30)
        self.emboss_button.place(x=60,y=175,width=140,height=30)
        self.gaussian_blur_button.place(x=60,y=230,width=140,height=30)
        self.median_blur_button.place(x=60,y=285,width=140,height=30)
        self.cancel_button.place(x=10,y=340,width=110,height=30)
        self.apply_button.place(x=130,y=340,width=110,height=30)

    def negative_button_released(self, event):
        self.negative()
        self.show_image()

    def black_white_released(self, event):
        self.black_white()
        self.show_image()

    def sepia_button_released(self, event):
        self.sepia()
        self.show_image()

    def emboss_button_released(self, event):
        self.emboss()
        self.show_image()

    def gaussian_blur_button_released(self, event):
        self.gaussian_blur()
        self.show_image()

    def median_blur_button_released(self, event):
        self.gaussian_blur()
        self.show_image()

    def apply_button_released(self, event):
        self.master.processed_image = self.filtered_image
        self.show_image()
        self.close()

    def cancel_button_released(self, event):
        self.master.image_viewer.show_image()
        self.close()

    def show_image(self):
        self.master.image_viewer.show_image(img=self.filtered_image)

    def negative(self):
        self.filtered_image = cv2.bitwise_not(self.original_image)

    def black_white(self):
        self.filtered_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        self.filtered_image = cv2.cvtColor(self.filtered_image, cv2.COLOR_GRAY2BGR)

    def sepia(self):
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])

        self.filtered_image = cv2.filter2D(self.original_image, -1, kernel)

    def emboss(self):
        kernel = np.array([[0, -1, -1],
                           [1, 0, -1],
                           [1, 1, 0]])

        self.filtered_image = cv2.filter2D(self.original_image, -1, kernel)

    def gaussian_blur(self):
        self.filtered_image = cv2.GaussianBlur(self.original_image, (41, 41), 0)

    def median_blur(self):
        self.filtered_image = cv2.medianBlur(self.original_image, 41)

    def close(self):
        self.destroy()

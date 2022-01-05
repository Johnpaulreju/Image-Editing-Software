from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os
import cv2
from tkinter import messagebox


class BorderFrame(Toplevel):

    def __init__(self, master=None):
        Toplevel.__init__(self, master=master, width="150", height="300")
        saveimg=Image.open(r"Images\bgimg.jpg")
        self.bgimg=ImageTk.PhotoImage(saveimg)
        self.label1 = Label(self,image=self.bgimg)
        self.label1.place(x=0, y=0)
        self.original_image = self.master.processed_image
        self.rotated_image = None
        
        self.border_10_button=Button(master=self, text="Border 10")
        self.border_45_button = Button(master=self, text="Border 45")
        self.border_90_button = Button(master=self, text="Border 90")
        self.close_button=Button(master=self,text="Close")
        self.cancel_button=Button(master=self,text="Cancel")


        self.border_10_button.bind("<ButtonRelease>", self.border_10_button_released)
        self.border_45_button.bind("<ButtonRelease>", self.border_45_button_released)
        self.border_90_button.bind("<ButtonRelease>", self.border_90_button_released)
        self.close_button.bind("<ButtonRelease>", self.close)
        self.cancel_button.bind("<ButtonRelease>", self.cancel_button_released)

        self.border_10_button.pack()
        self.border_45_button.pack()
        self.border_90_button.pack()
        self.close_button.pack()
        self.cancel_button.pack()

    def border_10_button_released(self,event):
        self.border_10()
        self.show_image()
        
    def border_45_button_released(self,event):
        self.border_45()
        self.show_image()

    def border_90_button_released(self,event):
        self.border_90()
        self.show_image()        

    def border_10(self):
        global img, imgg
        self.rotated_image=cv2.copyMakeBorder(self.original_image, 20, 20, 20, 20,cv2.BORDER_CONSTANT, value=[165,42,42])

    def border_45(self):
        global img, imgg
        self.rotated_image=cv2.copyMakeBorder(self.original_image, 50, 50, 50, 50,cv2.BORDER_CONSTANT, value=[165,42,42])

    def border_90(self):
        global img, imgg
        self.rotated_image=cv2.copyMakeBorder(self.original_image, 95, 95, 95, 95,cv2.BORDER_CONSTANT, value=[165,42,42])

    def show_image(self):
        self.master.image_viewer.show_image(img=self.rotated_image)

    def cancel_button_released(self, event):
        self.master.image_viewer.show_image()
        self.close()
    
    def close(self,event):
        self.destroy()
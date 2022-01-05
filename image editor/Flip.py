from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os
import cv2
from tkinter import messagebox


class FlipFrame(Toplevel):

    def __init__(self, master=None):
        Toplevel.__init__(self, master=master, width="150", height="300")
        saveimg=Image.open(r"Images\bgimg.jpg")
        self.bgimg=ImageTk.PhotoImage(saveimg)
        self.label1 = Label(self,image=self.bgimg)
        self.label1.place(x=0, y=0)

        self.original_image = self.master.processed_image
        self.rotated_image = None
        
        self.rotate_90_button=Button(master=self, text="Flip Bottom Up")
        self.rotate_180_button = Button(master=self, text="Flip Left To Right")
        self.rotate_270_button = Button(master=self, text="Flip L-R & B-U")
        self.close_button=Button(master=self,text="Close")
        self.cancel_button=Button(master=self,text="Cancel")


        self.rotate_90_button.bind("<ButtonRelease>", self.FLIP_BU_button_released)
        self.rotate_180_button.bind("<ButtonRelease>", self.FLIP_LR_button_released)
        self.rotate_270_button.bind("<ButtonRelease>", self.Flip_BU_LR_button_released)
        self.close_button.bind("<ButtonRelease>", self.close)
        self.cancel_button.bind("<ButtonRelease>", self.cancel_button_released)

        self.rotate_90_button.pack()
        self.rotate_180_button.pack()
        self.rotate_270_button.pack()
        self.close_button.pack()
        self.cancel_button.pack()

    def FLIP_BU_button_released(self,event):
        self.Flip_Bottom_Up()
        self.show_image()
        
    def FLIP_LR_button_released(self,event):
        self.Flip_Left_to_Right()
        self.show_image()

    def Flip_BU_LR_button_released(self,event):
        self.Flip_BU_LR()
        self.show_image()        

    def Flip_Bottom_Up(self):
        global img, imgg
        self.rotated_image=cv2.flip(self.original_image, 0)

    def Flip_Left_to_Right(self):
        global img, imgg
        self.rotated_image=cv2.flip(self.original_image, 1)

    def Flip_BU_LR(self):
        global img, imgg
        self.rotated_image=cv2.flip(self.original_image, -1)

    def show_image(self):
        self.master.image_viewer.show_image(img=self.rotated_image)

    def cancel_button_released(self, event):
        self.master.image_viewer.show_image()
        self.close()
    
    def close(self,event):
        self.destroy()
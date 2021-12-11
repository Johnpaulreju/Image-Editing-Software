from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os
import cv2
from tkinter import messagebox


class EditorFrame(Toplevel):

    def __init__(self, master=None):
        Toplevel.__init__(self, master=master, width="150", height="300")

        self.original_image = self.master.processed_image
        self.rotated_image = None
        
        self.rotate_90_button=Button(master=self, text="Rotate 90")
        self.rotate_180_button = Button(master=self, text="Rotate 180")
        self.rotate_270_button = Button(master=self, text="Rotate 270")
        self.close_button=Button(master=self,text="Close")
        self.cancel_button=Button(master=self,text="Cancel")


        self.rotate_90_button.bind("<ButtonRelease>", self.rotate_90_button_released)
        self.rotate_180_button.bind("<ButtonRelease>", self.rotate_180_button_released)
        self.rotate_270_button.bind("<ButtonRelease>", self.rotate_270_button_released)
        self.close_button.bind("<ButtonRelease>", self.close)
        self.cancel_button.bind("<ButtonRelease>", self.cancel_button_released)

        self.rotate_90_button.pack()
        self.rotate_180_button.pack()
        self.rotate_270_button.pack()
        self.close_button.pack()
        self.cancel_button.pack()

    def rotate_90_button_released(self,event):
        self.rotate_90()
        self.show_image()
        
    def rotate_270_button_released(self,event):
        self.rotate_270()
        self.show_image()

    def rotate_180_button_released(self,event):
        self.rotate_180()
        self.show_image()        

    def rotate_90(self):
        global img, imgg
        self.rotated_image=cv2.rotate(self.original_image,cv2.ROTATE_90_CLOCKWISE)

    def rotate_180(self):
        global img, imgg
        self.rotated_image=cv2.rotate(self.original_image,cv2.ROTATE_180)

    def rotate_360(self):
        global img, imgg
        self.rotated_image=cv2.rotate(self.original_image,cv2.ROTATE_90_CLOCKWISE)

    def rotate_270(self):
        global img, imgg
        self.rotated_image=cv2.rotate(self.original_image,cv2.ROTATE_90_COUNTERCLOCKWISE)

    def show_image(self):
        self.master.image_viewer.show_image(img=self.rotated_image)

    def cancel_button_released(self, event):
        self.master.image_viewer.show_image()
        self.close()
    
    def close(self):
        self.destroy()
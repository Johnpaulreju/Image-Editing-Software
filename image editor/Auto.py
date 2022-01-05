from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os
import cv2
from tkinter import messagebox

class AutoBar(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master=master, borderwidth = 2, width= 407, height=134,highlightbackground="black",highlightthickness=3, relief=RIDGE)
        autoimg=Image.open(r"Images\auto.jpg")
        autoimg=autoimg.resize((60,30),Image.ANTIALIAS)
        self.photoimgauto=ImageTk.PhotoImage(autoimg)        
        self.autolabel=Label(self, font=("Ariel 18 bold"),text="If you wanna let the software \nEdit for you. Please Kindly \nClick the Button Below THIS !!")
        self.autolabel.place(x=8,y=1)
        self.autobutt=Button(self,image=self.photoimgauto,cursor="hand2",command=self.auto_Button_Released)
        self.autobutt.place(x=145,y=90,width=60,height=30)

    def auto_Button_Released(self):
        messagebox.showinfo("Comming Soon..","This Function is nt currently available in this version ")

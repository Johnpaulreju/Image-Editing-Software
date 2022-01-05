from tkinter import *
import tkinter as tk

from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os
import cv2
from filterframe import Editorframe
from tkinter import messagebox
from imageview import ImageViewer
from button import EditBar
from purchase import PurchaseFrame
from Auto import AutoBar

class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.filename = ""
        self.original_image = None
        self.processed_image = None
        self.is_image_selected = False
        self.is_draw_state = False
        self.is_crop_state = False

        self.filter_frame = None
        self.adjust_frame = None
        self.geometry("920x628+0+0")
        self.iconbitmap(r"Images\logo1.ico")
        self.title("Image Editor by RCL")
        self.background='#249794'
        menu = Menu(self)
        self.config(menu=menu)
#  #  File menu formation in menubar
        filemenu = Menu(menu)
        menu.add_cascade(label='File', menu=filemenu)
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command = self.quit)

#  #  File menu formation in menubar
        Regimenu = Menu(menu)
        menu.add_cascade(label='Register', menu=Regimenu)
        Regimenu.add_command(label='Update',command=self.update)
        Regimenu.add_command(label='Purchase', command=self.purchase)

#  #  File menu formation in menubar
        helpmenu = Menu(menu)
        menu.add_cascade(label='Help', menu=helpmenu)
        helpmenu.add_command(label='About')

        self.editbar = EditBar(master=self)
        self.image_viewer = ImageViewer(master=self)
        self.editor= Editorframe(master=self)
        self.autobar = AutoBar(master=self)

        self.editbar.place(x=5,y=464)
        self.image_viewer.place(x=5,y=2)
        self.autobar.place(x=510,y=464)
        self.editor.place(x=808,y=2)

    def purchase(self):
        self.app=PurchaseFrame(master=self)

    def update(self):
        messagebox.showinfo("Update Details","No New Update Is Out")
            
   


from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import cv2
from filter import FilterFrame
from adjustbar import AdjustFrame



class EditBar(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master=master, borderwidth = 2, width= 500, height=133,highlightbackground="black",highlightthickness=3, relief=RIDGE)
        #####      Images for Frame 3
        saveimg=Image.open(r"Images\savebut.jpg")
        saveimg=saveimg.resize((40,40),Image.ANTIALIAS)
        self.photoimgsave=ImageTk.PhotoImage(saveimg)
        openimg=Image.open(r"Images\open.jpg")
        openimg=openimg.resize((40,40),Image.ANTIALIAS)
        self.photoimgopen=ImageTk.PhotoImage(openimg)
        cropimg=Image.open(r"Images\crop.jpg")
        cropimg=cropimg.resize((40,40),Image.ANTIALIAS)
        self.photoimgcrop=ImageTk.PhotoImage(cropimg)
        drawimg=Image.open(r"Images\draw.jpg")
        drawimg=drawimg.resize((40,40),Image.ANTIALIAS)
        self.photoimgdraw=ImageTk.PhotoImage(drawimg)
        redoimg=Image.open(r"Images\saveas.jpg")
        redoimg=redoimg.resize((40,40),Image.ANTIALIAS)
        self.photoimgredo=ImageTk.PhotoImage(redoimg)
        undoimg=Image.open(r"Images\undo.jpg")
        undoimg=undoimg.resize((40,40),Image.ANTIALIAS)
        self.photoimgundo=ImageTk.PhotoImage(undoimg)
        resetimg=Image.open(r"Images\reset.jpg")
        resetimg=resetimg.resize((40,40),Image.ANTIALIAS)
        self.photoimgreset=ImageTk.PhotoImage(resetimg)
        emojiimg=Image.open(r"Images\adjust.jpg")
        emojiimg=emojiimg.resize((40,40),Image.ANTIALIAS)
        self.photoimgemoji=ImageTk.PhotoImage(emojiimg)
        filterimg=Image.open(r"Images\filter.jpg")
        filterimg=filterimg.resize((80,80),Image.ANTIALIAS)
        self.photoimgfilter=ImageTk.PhotoImage(filterimg)

#####      Frame 3
        self.b1=Button(self,image=self.photoimgsave,cursor="hand2")
        self.b1.place(x=25,y=2,width=40,height=40)
        self.b1name = Label(self, text="SAVE", font=("Ariel 6"), anchor='e')
        self.b1name.place(x=30, y=43)
        self.b2=Button(self,image=self.photoimgopen,cursor="hand2")
        self.b2.place(x=25,y=65,width=40,height=40)
        self.b2name = Label(self, text="OPEN", font=("Ariel 6"), anchor='e')
        self.b2name.place(x=30, y=106)
        self.b3=Button(self,image=self.photoimgcrop,cursor="hand2")
        self.b3.place(x=120,y=2,width=40,height=40)
        self.b3name = Label(self, text="CROP", font=("Ariel 6"), anchor='e')
        self.b3name.place(x=125, y=43)
        self.b4=Button(self,image=self.photoimgdraw,cursor="hand2")
        self.b4.place(x=120,y=65,width=40,height=40)
        self.b4name = Label(self, text="DRAW", font=("Ariel 6"), anchor='e')
        self.b4name.place(x=125, y=106)
        self.b5=Button(self,image=self.photoimgredo,cursor="hand2")
        self.b5.place(x=215,y=65,width=40,height=40)
        self.b5name = Label(self, text="SAVE AS", font=("Ariel 6"), anchor='e')
        self.b5name.place(x=220, y=106)
        self.b6=Button(self,image=self.photoimgundo,cursor="hand2")
        self.b6.place(x=215,y=2,width=40,height=40)
        self.b6name = Label(self, text="UNDO", font=("Ariel 6"), anchor='e')
        self.b6name.place(x=220, y=43)
        self.b7=Button(self,image=self.photoimgreset,cursor="hand2")
        self.b7.place(x=310,y=2,width=40,height=40)
        self.b7name = Label(self, text="RESET", font=("Ariel 6"), anchor='e')
        self.b7name.place(x=315, y=43)
        self.b8=Button(self,image=self.photoimgemoji,cursor="hand2")
        self.b8.place(x=310,y=65,width=40,height=40)
        self.b8name = Label(self, text="ADJUST", font=("Ariel 6"), anchor='e')
        self.b8name.place(x=312, y=106)
        self.b9=Button(self,image=self.photoimgfilter,cursor="hand2")
        self.b9.place(x=390,y=5,width=80,height=80)
        self.b9name = Label(self, text="FILTER", font=("Ariel 12"), anchor='e')
        self.b9name.place(x=400, y=90)

        self.b2.bind("<ButtonRelease>", self.new_button_released)
        self.b1.bind("<ButtonRelease>", self.save_button_released)
        self.b4.bind("<ButtonRelease>", self.draw_button_released)
        self.b3.bind("<ButtonRelease>", self.crop_button_released)
        self.b7.bind("<ButtonRelease>", self.clear_button_released)
        self.b8.bind("<ButtonRelease>", self.adjust_button_released)
        self.b9.bind("<ButtonRelease>", self.filter_button_released)
        self.b5.bind("<ButtonRelease>", self.save_as_button_released)
    def save_as_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.save_as_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                original_file_type = self.master.filename.split('.')[-1]
                filename = filedialog.asksaveasfilename()
                filename = filename + "." + original_file_type

                save_image = self.master.processed_image
                cv2.imwrite(filename, save_image)

                self.master.filename = filename

    def filter_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.b9:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                self.master.filter_frame = FilterFrame(master=self.master)
                self.master.filter_frame.grab_set()

    def adjust_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.b8:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                self.master.adjust_frame = AdjustFrame(master=self.master)
                self.master.adjust_frame.grab_set()


    def new_button_released(self, event):
        global filename
        if self.winfo_containing(event.x_root, event.y_root) == self.b2:
            if self.master.is_draw_state:
                self.master.image_viewer.deactivate_draw()
            if self.master.is_crop_state:
                self.master.image_viewer.deactivate_crop()

            filename = filedialog.askopenfilename()
            image = cv2.imread(filename)

            if image is not None:
                self.master.FileName = filename
                self.master.original_image = image.copy()
                self.master.processed_image = image.copy()
                self.master.image_viewer.show_image()
                self.master.is_image_selected = True

    def save_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.b1:
            if self.master.is_image_selected:
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()

                save_image = self.master.processed_image
                image_filename = self.master.FileName
                cv2.imwrite(image_filename, save_image)

    def draw_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.b4:
            if self.master.is_image_selected:
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                else:
                    self.master.image_viewer.activate_draw()

    def crop_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.b3:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()
                else:
                    self.master.image_viewer.activate_crop()

    def clear_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.b7:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                self.master.processed_image = self.master.original_image.copy()
                self.master.image_viewer.show_image()

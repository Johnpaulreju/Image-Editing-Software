from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
import cv2
from Editor import EditorFrame
from border import BorderFrame
from Flip import FlipFrame


class Editorframe(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master=master, borderwidth = 2, width= 107, height=460,bg='#249794',highlightbackground="black",highlightthickness=3, relief=RIDGE)
        self.rotate_button = Button(self, text="ROTATE",borderwidth=2,fg = 'black',
                 bg = 'yellow',font = (("Times New Roman"),15))
        self.rotate_button.bind("<ButtonRelease>", self.rotate_button_released)
        self.rotate_button.place(x=3,y=80,width=90,height=50)

        self.border_button = Button(self, text="BORDER",borderwidth=2,fg = 'black',
                 bg = 'yellow',font = (("Times New Roman"),15))
        self.border_button.bind("<ButtonRelease>", self.border_button_released)
        self.border_button.place(x=3,y=180,width=90,height=50)

        self.flip_button = Button(self, text="FLIP",borderwidth=2,fg = 'black',
                 bg = 'yellow',font = (("Times New Roman"),15))
        self.flip_button.bind("<ButtonRelease>", self.flip_button_released)
        self.flip_button.place(x=3,y=280,width=90,height=50)

    def rotate_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.rotate_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                self.master.filter_frame = EditorFrame(master=self.master)
                self.master.filter_frame.grab_set()

    def border_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.border_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                self.master.filter_frame = BorderFrame(master=self.master)
                self.master.filter_frame.grab_set()

    def flip_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.flip_button:
            if self.master.is_image_selected:
                if self.master.is_draw_state:
                    self.master.image_viewer.deactivate_draw()
                if self.master.is_crop_state:
                    self.master.image_viewer.deactivate_crop()

                self.master.filter_frame = FlipFrame(master=self.master)
                self.master.filter_frame.grab_set()
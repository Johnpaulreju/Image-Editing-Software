from tkinter.ttk import Progressbar
from tkinter import *
from tkinter import ttk
from main import Main
from PIL import Image, ImageTk
w=Tk()


width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))


w.overrideredirect(1)


s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
progress=Progressbar(w,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate',)

#############progressbar          33333333333333333333333333333
def new_win():
  # w.destroy()
    root = Main()
    root.mainloop()

def bar():

    l4=Label(w,text='Loading...',fg='white',bg=a)
    lst4=('Calibri (Body)',10)
    l4.config(font=lst4)
    l4.place(x=18,y=210)
    
    import time
    r=0
    for i in range(100):
        progress['value']=r
        w.update_idletasks()
        time.sleep(0.03)
        r=r+1
    
    w.destroy()
    new_win()
        
    
progress.place(x=-10,y=235)

a='#249794'
f2=Frame(w,width=290,height=241,bg=a).place(x=0,y=0)  #249794
b1=Button(w,width=10,height=1,text='Get Started',command=bar,border=0,fg=a,bg='white')
b1.place(x=170,y=200)
saveimg=Image.open(r"Images\newbg.jpg")
saveimg=saveimg.resize((170,240),Image.ANTIALIAS)
bgimg=ImageTk.PhotoImage(saveimg)
Label(w,image=bgimg,bg=a).place(x=260, y=-2)
######## Label
iconimg=Image.open(r"Images\icon.jpg")
iconimg=iconimg.resize((60,60),Image.ANTIALIAS)
iconimg=ImageTk.PhotoImage(iconimg)
l1=Label(w,image=iconimg,bg=a).place(x=180, y=2)

l1=Label(w,text='IMAGE EDITOR',fg='white',bg=a)
lst1=('Calibri (Body)',18,'bold')
l1.config(font=lst1)
l1.place(x=30,y=80)

l3=Label(w,text='V 0.1.0',fg='white',bg=a)
lst3=('Algerian',10)
l3.config(font=lst3)
l3.place(x=30,y=110)

  


w.mainloop()



from tkinter import *
from PIL import Image, ImageTk
import smtplib
from tkinter import messagebox
import os

class PurchaseFrame(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master, width="300", height="200")
        saveimg=Image.open(r"Images\bgimg.jpg")
        self.bgimg=ImageTk.PhotoImage(saveimg)
        self.label1 = Label(self,image=self.bgimg)
        self.label1.place(x=0, y=0)
        self.label2=Label(self,text="SELECT YOUR CHOICE",bg="blue", font=("Ariel 13")).place(x=1,y=1,width=300,height=40)

        self.but1=Button(self,text="LOGIN",borderwidth=2,cursor="hand2",fg = 'black',
                 bg = 'yellow',font = (("Times New Roman"),15),command = self.login).place(x=80,y=70,width=150,height=40)

        self.but2=Button(self,text="REGISTER",borderwidth=2,cursor="hand2",fg = 'black',
                 bg = 'yellow',command = self.register,font = (("Times New Roman"),15)).place(x=80,y=130,width=150,height=40)

    def register(self):
        global register_screen
        register_screen = Toplevel()
        saveimg=Image.open(r"Images\bgimg.jpg")
        self.bgimg=ImageTk.PhotoImage(saveimg)
        self.label1 = Label(register_screen,image=self.bgimg)
        self.label1.place(x=0, y=0)
        register_screen.title("Register")
        register_screen.geometry("400x290")
    
        global username
        global password
        global emailname
        global username_entry
        global password_entry
        global email_entry
        username = StringVar()
        password = StringVar()
        emailname= StringVar()
    
        Label(register_screen, text="*PLEASE ENTER YOUR DETAILS*",bg="blue", font=("Ariel 13")).place(x=2,y=0,width=400,height=40)
        username_lable = Label(register_screen, text="USERNAME-:", font=("Arial 15"))
        username_lable.place(x=10,y=60,width=140,height=30)
        username_entry = Entry(register_screen, textvariable=username)
        username_entry.place(x=170,y=60,width=190,height=30)
        email_lable = Label(register_screen, text="EMAIL-:", font=("Arial 15"))
        email_lable.place(x=10,y=110,width=90,height=30)
        email_entry = Entry(register_screen, textvariable=emailname)
        email_entry.place(x=105,y=110,width=190,height=30)
        Label(register_screen,text="@Gmail.com", font=("Arial 10")).place(x=298,y=110,width=80,height=30)
        password_lable = Label(register_screen, text="PASSWORD-:", font=("Arial 15"))
        password_lable.place(x=10,y=160,width=140,height=30)
        password_entry = Entry(register_screen, textvariable=password, show='*')
        password_entry.place(x=160,y=160,width=190,height=30)
        Button(register_screen, text="REGISTER", width=10, height=1,
                font=("Arial 15"),bg="blue", command =lambda:[self.register_user(),self.email_user()]).place(x=130,y=210,width=150,height=40)
    
    # Designing window for login 
    def email_user(self):
        try:
            reciver=emailname.get()
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login('bcaproject2k21@gmail.com','sirrfnmvsmgyycsq')
            server.sendmail('bcaproject2k21@gmail.com',reciver+'@gmail.com','Thank you for using Our Software')
            print("emailsent")
        except:
            messagebox.showerror("Warning","Please Enter The Email First")
 
    def login(self):
        global login_screen
        login_screen = Toplevel()
        saveimg=Image.open(r"Images\bgimg.jpg")
        self.bgimg=ImageTk.PhotoImage(saveimg)
        self.label1 = Label(login_screen,image=self.bgimg)
        self.label1.place(x=0, y=0)
        login_screen.title("Login")
        login_screen.geometry("380x280")
        Label(login_screen, text="PLEASE ENTER DETAILS BELOW TO LOGIN",bg="blue", font=("Ariel 13")).place(x=0,y=0,width=380,height=50)
    
        global username_verify
        global password_verify
    
        username_verify = StringVar()
        password_verify = StringVar()
    
        global username_login_entry
        global password_login_entry
    
        Label(login_screen, text="USERNAME -:", font=("Algerian 15")).place(x=10,y=80,width=150,height=30)
        username_login_entry = Entry(login_screen, textvariable=username_verify, font=("Arial 15"))
        username_login_entry.place(x=170,y=80,width=190,height=30)
        Label(login_screen, text="Password-:",bg="blue", font=("Algerian 15")).place(x=10,y=150,width=150,height=30)
        password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
        password_login_entry.place(x=170,y=150,width=190,height=30)
        Button(login_screen, text="LOGIN",command = self.login_verify, borderwidth=2,cursor="hand2"
                    ,bg = 'yellow',font =(("Times New Roman"),15)).place(x=120,y=200,width=150,height=40)
    
    # Implementing event on register button
    
    def register_user(self):
        username_info = username.get()
        password_info = password.get()
        file = open(username_info, "w")
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()
        messagebox.showinfo("Registered","You Are Now Registered To Our Software")
        username_entry.delete(0, END)
        password_entry.delete(0, END)
    
    # Implementing event on login button 
    
    def login_verify(self):
        username1 = username_verify.get()
        password1 = password_verify.get()
        username_login_entry.delete(0, END)
        password_login_entry.delete(0, END)
    
        list_of_files = os.listdir()
        if username1 in list_of_files:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                messagebox.showinfo("Success","Loged In Successfully")
    
            else:
                messagebox.showwarning("Warning","Password Incorrect")
    
        else:
            messagebox.showerror("Error","User Not Found")

from cgitb import text
# from curses import window
from sys import dont_write_bytecode
from tkinter import *
from turtle import back, home, width, window_width
from PIL import ImageTk , Image
import os
import signup


class homePage : 
    def __init__(self,window,institution = ""):
        self.window = window
        self.window.geometry('1166x718')
        menu = Menu(window)
        window.config(menu=menu , bg='#27285C')

# =============help menu=================
        helpMenu = Menu(menu , tearoff=0 , activebackground='orange')
        helpMenu.add_command(label='how to use')
        helpMenu.add_command(label='about us')
        menu.add_cascade(label='help' , menu=helpMenu)

# =============setting menu=================      
        settingMenu = Menu(menu , tearoff=0 , activebackground='orange')
        settingMenu.add_command(label='account setting')
        settingMenu.add_command(label='log out')
        menu.add_cascade(label='setting' , menu=settingMenu)

# =============exit menu=================      
        exitMenu = Menu(menu , tearoff=0 , activebackground='orange')
        menu.add_cascade(label='exit' , menu=exitMenu)

# =============logo =================           
        self.logo = Image.open('images\\login_bg.jpg')
        photo = ImageTk.PhotoImage(self.logo)
        self.logo_panel = Label(self.window,image=photo)
        self.logo_panel.image = photo
        self.logo_panel.place(x=458 , y=50 , width=250 , height=250 )  

# =============profile =================           
        self.profile_wlc = Label(self.window , font=(100) , bg='#27285C' , fg='white' , text="Welcome back!" , justify='center')
        self.profile_wlc.place(x=358 , y=320 , width=450)

        self.profile = Label(self.window , font=(100) , bg='#27285C' , fg='white' , text="This security camera is currently working for "+ institution , justify='center')
        self.profile.place(x=258 , y=350 , width=650)

# =============recording button =================        
        self.record_button = Button(self.window , text='Start recording' , font=(50)  , cursor='hand2' , command=startRecording)
        self.record_button.place(x=458,y=400 , width=250 , height=150 )
        self.record_button.bind('<Enter>' , on_enter)
        self.record_button.bind('<Leave>' , on_leave)

    def page(self):
        self.window.mainloop()

def startRecording():
        os.system('python site-packages\cam.py')

def on_enter(e):
   e.widget['background']='violet'
   e.widget['foreground']= "white"

def on_leave(e):
   e.widget['background']='#1995CC'
   e.widget['foreground']= "black"

#    https://stackoverflow.com/questions/49888623/tkinter-hovering-over-button-color-change
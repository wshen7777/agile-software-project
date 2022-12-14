from cgitb import text
from csv import reader
from tkinter import *
from tkinter import messagebox
from turtle import back, window_width
from PIL import ImageTk , Image
import os
import signup
from setuptools import *
import csv
import home
import json
import resetPassword

class loginForm : 
    def __init__(self,window):
        self.user_email = None
        self.user_password = None
        self.user_institution = None
        self.window = window
        self.window.geometry('1166x718')
        # self.window.state('zoomed')

        # ========= background =========
        self.bg_frame = Image.open('images\\login_bg.jpg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window,image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both' , expand='yes')

        # ========= login frame =========
        self.lg_frame = Frame(self.window , width=650 , height=600 , bg='black')
        self.lg_frame.place(x=258,y=70)

        # ========= logo =========
        self.logo_frame = Image.open('images\\logo.jpg')
        logo_photo = ImageTk.PhotoImage(self.logo_frame)
        self.logo = Label(self.lg_frame , image=logo_photo) 
        self.logo.image = logo_photo
        self.logo.place(x=250 , y=80 , width=150 , height=150)

        # ========= email =========
        self.email_label = Label(self.lg_frame , text='Email Address : ' , bg='black' , font=(30) , fg='white')
        self.email_label.place(x=250 , y= 250 , width=150 , height=20)   

        self.email_textbox = Entry(self.lg_frame , font=(25) , bg='black' , relief='flat' , highlightthickness=0 , fg='white' , insertbackground='white')
        self.email_textbox.place(x=200 , y=280 , width=250 , height=20)

        self.email_line = Canvas(self.lg_frame , width= 250 , height=2 , bg='white' , highlightthickness=0 )
        self.email_line.place(x=200 , y=300)

        # ========= password =========
        self.password_label = Label(self.lg_frame , text='Password : ' , bg='black' , font=(30) , fg='white')
        self.password_label.place(x=250 , y= 320 , width=150 , height=20)   

        self.password_textbox = Entry(self.lg_frame , font=(25) , bg='black' , relief='flat' , show='*' , fg='white' , insertbackground='white')
        self.password_textbox.place(x=200 , y=350 , width=250 , height=20)

        self.password_line = Canvas(self.lg_frame , width= 250 , height=2 , bg='white' , highlightthickness=0 )
        self.password_line.place(x=200 , y=370)

        # ========= login button =========
        self.login_button = Image.open('images\\login_button.png')
        login_button_photo = ImageTk.PhotoImage(self.login_button)
        self.login_button_label = Label(self.lg_frame , image= login_button_photo , bg='black')
        self.login_button_label.image = login_button_photo
        self.login_button_label.place(x=200 , y=400 , width=250 , height=50)

        self.login = Button(self.login_button_label , text='login' , font=(25) , bd=0 , cursor='hand2' , activeforeground='grey' , activebackground= '#1995CC', fg='black' , background='#1995CC' , command=lambda : self.validateAccount(self.email_textbox,self.password_textbox))
        self.login.place(x=55,y=10 ,width=130 , height=30)

        # ========= sign up =========
        self.signup = Label(self.lg_frame , text="Don't have an account?" , bg='black' , fg='white')
        self.signup.place(x=220 , y=455 , height=14)

        self.signup_link = Label(self.lg_frame , text="sign up now" , bg='black' , font= ('Helvetica 10 underline') , cursor='hand2', fg='#ADD8E6')
        self.signup_link.place(x=350 , y=455 , height=14)
        
        self.signup_link.bind('<Button-1>' , lambda event:self.loadSignupPage())
        
        # ========= forget password =========
        self.forget_pw = Label(self.lg_frame , text="forget password?" , bg='black' , font= ('Helvetica 10 underline') , cursor='hand2', fg='#99f8d3')
        self.forget_pw.place(x=270 , y=475 , height=14)

        self.forget_pw.bind('<Button-1>' , lambda event:self.loadForgetPage())

    def validateAccount(cls , email_entry , password_entry):
        if email_entry.get() == '' or password_entry.get()=='' :
            messagebox.showerror(title="Error" , message="Please fill in your email or password")
            return
        
        if os.path.exists('users_account.csv'):
            with open('users_account.csv','r',newline='') as f:
                reader = csv.reader(f)
                for row in reader :
                    if (row[1]== email_entry.get() and row[2] == password_entry.get()):
                        cls.user_institution = row[0]
                        cls.user_email = row[1]
                        cls.user_password = row[2]
                        user_dict= {"insti_name" : cls.user_institution , "user_email":cls.user_email , "user_password":cls.user_password}
                        with open("logging_in.json", "w") as outfile:
                            json.dump(user_dict, outfile)
                        for widgets in cls.window.winfo_children():
                            widgets.destroy()
                        homePage = home.homePage(cls.window , institution=cls.user_institution)
                        homePage.loadPage()
                        return
            messagebox.showerror(title="Error" , message="Invalid email or password")
    
    def loginPage(self):
        self.window.mainloop()
    
    def loadSignupPage(self):
        for widgets in self.window.winfo_children():
            widgets.destroy()
        signUpPage=signup.signupForm(self.window)
        signUpPage.signupPage() 

    def loadForgetPage(self):
        for widgets in self.window.winfo_children():
            widgets.destroy()
        forgetPage=resetPassword.resetPage(self.window)
        forgetPage.loadPage()
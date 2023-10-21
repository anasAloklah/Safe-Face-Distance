from tkinter import *
from tkinter import messagebox,Button
import tkinter as tk
from os import path
class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        Label(self, text='user name  :').grid(row=0)
        Label(self, text='password   :').grid(row=1)
        self.userNameEntry = Entry(self)
        self.passWordEntry = Entry(self, show="*")
        self.userNameEntry.grid(row=0, column=1)
        self.passWordEntry.grid(row=1, column=1)
        self.logIn = Button(self, text='Log in ', width=15, command=self.DoLogin).grid(row=2)
        self.forgetPassword = Button(self, text='forget password ', width=15, command=self.GoToSecretQuestion).grid(row=2, column=1)

    def DoLogin(self):
        if path.exists('data.txt'):
            f = open("data.txt", "r")
            data=f.read().split('|')
            f.close()
            userName=data[0]
            password=data[1]
            if self.passWordEntry.get() == password and self.userNameEntry.get() == userName:
                self.controller.show_frame("SecondPage")
            else:
                messagebox.showerror(title="wrong message", message="the user name or password is wrong")
        else:
            userName=self.userNameEntry.get()
            password=self.passWordEntry.get()
            f = open("data.txt", "w")
            f.write(userName + '|' + password)
            f.close()
            self.controller.show_frame("SecondPage")
    def GoToSecretQuestion(self):
        self.controller.show_frame("SecretQuestionPage")
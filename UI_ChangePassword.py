from tkinter import *
from tkinter import messagebox,Button
import tkinter as tk
class ChangePassword(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        Label(self, text='old password            :').grid(row=0)
        Label(self, text='new password            :').grid(row=2)
        Label(self, text='re input new password   :').grid(row=3)
        self.oldPassWordEntry = Entry(self, show="*")
        self.newPassWordEntry = Entry(self, show="*")
        self.renewPassWordEntry = Entry(self, show="*")
        self.oldPassWordEntry.grid(row=0, column=1)
        self.newPassWordEntry.grid(row=2, column=1)
        self.renewPassWordEntry.grid(row=3, column=1)
        self.button = Button(self, text='change', width=15, command=self.DoChange).grid(row=4)
        self.btn = Button(self, text='back', width=15, command=lambda: controller.show_frame("SecondPage")).grid(row=5)

    def DoChange(self):
        f = open("data.txt", "r")
        data=f.read().split('|')
        userName=data[0]
        password=data[1]
        if self.oldPassWordEntry.get()!="":
            if self.oldPassWordEntry.get() == password:
                if self.newPassWordEntry.get() == self.renewPassWordEntry.get():
                    messagebox.showinfo(title="change password", message="scussed")
                    f = open("data.txt", "w")
                    f.write(userName+'|'+self.newPassWordEntry.get())
                    f.close()
                else:
                    messagebox.showerror(title="wrong message", message="the two new password is not same")
            else:
                messagebox.showerror(title="wrong message", message="the old password is wrong")
        else:
            messagebox.showerror(title="wrong message", message="enter the old password")
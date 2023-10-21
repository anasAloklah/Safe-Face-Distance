from tkinter import *
from tkinter import messagebox,Button
import tkinter as tk
from UI_RunProgram import RunProgram
from  UI_Registration import Registration
from os import path
class SecondPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.btn_run = Button(self, text='Run Program', width=15,command=self.goToRun)
        self.btn_changePassWord = Button(self, text='change password', width=15,command=self.goToChangePassword)
        self.btn_run.pack()
        self.btn_changePassWord.pack()



    def goToRun(self):
        if path.exists('measurement.txt'):
            self.controller.show_frame2(RunProgram)
        else:
            self.controller.show_frame2(Registration)
    def goToChangePassword(self):
        self.controller.show_frame("ChangePassword")


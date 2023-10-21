from tkinter import *
from tkinter import messagebox,Button
import tkinter as tk
from UI_RunProgram import RunProgram
from  UI_Registration import Registration
from os import path
class SecretQuestionPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.secretQuestion = Label(self, text='what is your Profesor name:', font=("Helvetica 12 bold"))
        self.secretQuestion.pack()
        self.answerOfSecretQuestion = Entry(self)
        self.answerOfSecretQuestion.pack()
        self.btn_answer = Button(self, text='answer', width=15,command=self.doAnswer)
        self.btn_answer.pack()
        self.userName = Label(self, text='user name:', font=("Helvetica 12 bold"))
        self.userName.pack()
        self.password = Label(self, text='password:', font=("Helvetica 12 bold"))
        self.password.pack()
        self.btn_back = Button(self, text='back', width=15, command=self.goToLogIn)
        self.btn_back.pack()

    def doAnswer(self):
        f = open("data.txt", "r")
        data=f.read().split('|')
        userName=data[0]
        password=data[1]
        if self.answerOfSecretQuestion.get() != "":
            if self.answerOfSecretQuestion.get() == "khaled":
                self.userName.config(text='user name:' + str(userName))
                self.password.config(text='password:' + str(password))
            else:
                messagebox.showerror(title="wrong message", message="the answer is wrong")
        else:
            messagebox.showerror(title="wrong message", message="enter the secret answer")

    def goToLogIn(self):
        self.controller.show_frame("LoginPage")


import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
from UI_Login import LoginPage
from UI_second_page import SecondPage
from UI_ChangePassword import ChangePassword

class StartApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.container = tk.Frame(self)
        self.title("safe distance")
        self.container.pack(side="top", fill="both", expand=True)
        self.frames = {}
        for F in (LoginPage,SecondPage,ChangePassword):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def show_frame2(self, framePage):
        framePage=framePage(parent=self.container, controller=self)
        framePage.grid(row=0, column=0, sticky="nsew")
        framePage.tkraise()

if __name__ == "__main__":
    app = StartApp()
    app.mainloop()
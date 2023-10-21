from tkinter import *
from tkinter import messagebox,Button
import tkinter as tk
import PIL
from PIL import Image,ImageTk
from mtcnn.mtcnn import MTCNN
from functions import distanceBetweenTowPoint,taskIsRun
import cv2
from tkinter import *
import os
from ctypes import *
import subprocess
class RunProgram(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.protocol('WM_DELETE_WINDOW', self.doNothing)
        self.cam = cv2.VideoCapture(0)
        self.face_detector = MTCNN()
        self.dis = 0
        self.saveDistance = 50
        self.run_screen_saver = True
        self.close_screen_saver = False
        self.l_Image = Label(self)
        self.l_Image.pack()
        self.l_eyes = Label(self, text='distance between two eyes:', font=("Helvetica 16 bold"))
        self.l_eyes.pack()
        self.l_dis_cam = Label(self, text='distance from screen:', font=("Helvetica 16 bold"))
        self.l_dis_cam.pack()
        self.PassWordEntry = Entry(self, show="*")
        self.PassWordEntry.pack()
        self.btn_close= Button(self, text='close', width=15, command=self.closeProgram)
        self.btn_close.pack()
        f = open("measurement.txt", "r")
        data = f.read().split('|')
        f.close()
        self.distanceBetweenEyesInEquation = data[1]
        self.distanceBetweenEyesInEquation = float(self.distanceBetweenEyesInEquation)
        self.show_frame()

    def show_frame(self):
        _, frame = self.cam.read()
        frame = cv2.flip(frame, 1)
        rgb_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        predction = self.face_detector.detect_faces(rgb_img)

        img = frame
        try:
            x, y, w, h = predction[0]['box']
            Elx, Ely = predction[0]['keypoints']['left_eye']
            Erx, Ery = predction[0]['keypoints']['right_eye']
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            img = cv2.rectangle(img, (Erx - 5, Ery - 5), (Erx + 5, Ery + 5), (0, 255, 0), 1)

            img = cv2.rectangle(img, (Elx - 5, Ely - 5), (Elx + 5, Ely + 5), (0, 255, 0), 1)

            dis_eyes = distanceBetweenTowPoint(Elx, Ely, Erx, Ery)  # distance by pixel

            dis_screen = float("{:.2f}".format(dis_eyes))
            self.l_eyes.config(text='distance between two eyes: ' + str(dis_screen)+" pixel")
            self.dis = (60 / (dis_screen / self.distanceBetweenEyesInEquation))
            self.dis = float("{:.2f}".format(self.dis))
            self.l_dis_cam.config(text='distance from screen:' + str(self.dis)+" cm")
            if self.dis < self.saveDistance and self.run_screen_saver:
                os.startfile("scrnsave.scr")
                windll.user32.BlockInput(True) # disable mouse and keyboard
                self.run_screen_saver = False
                self.close_screen_saver = True
            if self.dis > self.saveDistance and self.close_screen_saver:
                CREATE_NO_WINDOW = 0x08000000
                subprocess.call('taskkill /F /IM scrnsave.scr', creationflags=CREATE_NO_WINDOW)
                #os.system("TASKKILL /F /IM scrnsave.scr")
                windll.user32.BlockInput(False) # enable  mouse and keyboard
                self.run_screen_saver = True
                self.close_screen_saver = False

        except:
            self.dis = self.dis
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = PIL.Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        self.l_Image.imgtk = imgtk
        self.l_Image.configure(image=imgtk)
        self.l_Image.after(10, self.show_frame)
    def doNothing(self):
        x=""
    def closeProgram(self):
        f = open("data.txt", "r")
        data = f.read().split('|')
        password = data[1]
        if  self.PassWordEntry.get() == password:
            self.destroy()
            self.controller.destroy()
            self.cam.release()

from tkinter import *
from tkinter import messagebox,Button
import tkinter as tk
import PIL
from PIL import Image,ImageTk
from mtcnn.mtcnn import MTCNN
from functions import distanceBetweenTowPoint,convertInchToCm
import cv2
from tkinter import *
from UI_RunProgram import RunProgram
import os
import time
class Registration(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.cam = cv2.VideoCapture(0)
        self.face_detector = MTCNN()
        self.start = time.time()
        self.distanceBetweenEyes=0
        self.l_Image = Label(self)
        self.l_Image.pack()
        self.Calibration = Label(self, text='Calibration', font=("Helvetica 12 bold"))
        self.Calibration.pack()
        self.l_initial_distance_message = Label(self, text='please adiust the initial distance between your and camera by 60 cm', font=("Helvetica 12 bold"))
        self.l_initial_distance_message.pack()
        self.l_eyes = Label(self, text='Initial distance eyes:', font=("Helvetica 12 bold"))
        self.l_eyes.pack()
        self.distanceBetweenEyesEntry = Entry(self, show="")
        self.distanceBetweenEyesEntry.pack()
        self.registrationBtn= Button(self, text='Registration', width=15, command=self.registration)
        self.registrationBtn.pack()
        self.dis_screen =0
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
            self.dis_screen = float("{:.2f}".format(dis_eyes))
            self.distanceBetweenEyesEntry.delete(0, tk.END)
            self.distanceBetweenEyesEntry.insert(0,str(self.dis_screen))


        except:
            self.dis_screen = self.dis_screen
        end = time.time()
        if end-self.start <10:
            img = cv2.imread('info.jpg')
        background = cv2.imread('message_img.jpg')

        import numpy as np

        # create an overlay image. You can use any image
        foreground = np.ones((100, 100, 3), dtype='uint8') * 255
        added_image = cv2.addWeighted(img[430:470, 0:640, :], 0, background[0:40, 0:640, :], 1 - 0, 0)
        #added_image  = cv2.addWeighted(img[150:250,150:250,:],0,foreground[0:100,0:100,:],1-0,0)
        img[430:470, 0:640] = added_image
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = PIL.Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        self.l_Image.imgtk = imgtk
        self.l_Image.configure(image=imgtk)
        self.l_Image.after(10, self.show_frame)

    def registration(self):
        distanceBetweenInScreen = self.distanceBetweenEyesEntry.get()
        f = open("measurement.txt", "w")
        f.write(str('60') + '|' + str(distanceBetweenInScreen))
        f.close()

        self.cam.release()
        self.controller.show_frame2(RunProgram)


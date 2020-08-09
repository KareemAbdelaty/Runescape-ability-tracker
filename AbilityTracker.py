from collections import deque
from tkinter import *
from actionbar import actionbar
from tkinter import *
from PIL import Image, ImageTk
class AbilityTracker(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master,controller):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.labels =[0]*8
        self.queue = deque()
        load = Image.open("abilityImages/noImg.png")
        load = load.resize((95,45),Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        for i in range(8):
            self.queue.append(render)
            self.labels[i] = Label(self, image=render)
            self.labels[i].image = render
            self.labels[i].pack(side = LEFT)

    def showImg(self,image):
        self.queue.popleft()
        load = Image.open(image)
        load = load.resize((95,45),Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        self.queue.append(render)
        for i in range(8):
            self.labels[i].configure(image = self.queue[i])
            self.labels[i].image = self.queue[i] 

    def showText(self):
        text = Label(self, text="Hey there good lookin!")
        text.pack()
        

    def client_exit(self):
        exit()

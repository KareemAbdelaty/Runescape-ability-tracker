from tkinter import *
from AbilityTracker import *

class WindowManager(Tk):

    def __init__(self):
        
        Tk.__init__(self)
        self.init_interface()

    def show_frame(self, cont):
        frame  = self.currentFrame
        frame.pack_forget()
        frame = self.frames[cont]
        frame.pack(fill ='both',expand = True)
        self.currentFrame = frame
    def init_interface(self):
        container = Frame(self)
        self.title("Ability tracker")
        self.geometry("800x299")

        container.pack(side="top", fill="both", expand = True)
        self.frames = {}
        for F in (MainMenu,AbilityTracker, Setup,options):

            frame = F(container, self)

            self.frames[F] = frame

        self.currentFrame = self.frames[MainMenu]
        self.show_frame(MainMenu)



class options(Frame):

    def __init__(self,master,controller):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)
        self.controller = controller
        #reference to the master widget, which is the tk window
        self.master = master
        self.init_window()

    def init_window(self):
        self.brews = IntVar()
        self.food = IntVar()
        self.vigour = IntVar()
        self.fourtick = IntVar()
        self.mouse = IntVar()
        self.apm = IntVar()
        self.flanking = IntVar()
        self.lunging = IntVar()
        self.trackbrews = Checkbutton(self,text = "Track Brews" ,variable =self.brews)
        self.trackfood = Checkbutton(self,text = "Track Food" ,variable =self.food)
        self.trackvigour = Checkbutton(self,text = "Track Ring of Vigour" ,variable =self.vigour)
        self.track4tick = Checkbutton(self,text = "Track 4taa efficeny" ,variable =self.fourtick)
        self.trackapm = Checkbutton(self,text = "Track Actions Per Minute" ,variable =self.apm)
        self.trackmouse = Checkbutton(self,text = "Track Mouse Clicks" ,variable =self.mouse)
        self.trackflanking = Checkbutton(self,text = "Track Actions Per Minute" ,variable =self.flanking)
        self.tracklunging = Checkbutton(self,text = "Track Mouse Clicks" ,variable =self.lunging)
        self.trackbrews.grid(row = 1,column =2,sticky = W)
        self.trackfood.grid(row =2,column =2,sticky= W)
        self.trackvigour.grid(row =3,column =2,sticky= W)
        self.track4tick.grid(row =4,column =2,sticky= W)
        self.trackapm.grid(row = 5,column =2,sticky= W)
        self.trackmouse.grid(row = 6,column =2,sticky= W)
        self.trackflanking.grid(row = 7,column =2,sticky= W)
        self.tracklunging.grid(row = 8,column =2,sticky= W)
        self.back = Button(self,text = "back" ,command =lambda: self.controller.show_frame(MainMenu))
        self.back.grid(row =1,column =1,sticky= W)







class MainMenu(Frame):

    def __init__(self,master,controller):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)
        self.controller = controller
        #reference to the master widget, which is the tk window
        self.master = master
        self.init_window()

    def init_window(self):
        self.launch = Button(self,text = "Launch Tracker" ,command =lambda: self.controller.show_frame(AbilityTracker))
        self.options = Button(self, text = "Options" ,command =lambda: self.controller.show_frame(options))
        self.setup = Button(self,text = " Setup" , command =lambda: self.controller.show_frame(Setup))
        # self.launch.grid(row = 1,columnspan = 4)
        # self.options.grid(row=5,columnspan = 4)
        # self.setup.grid(row=7,columnspan = 4)
        self.launch.pack()
        self.options.pack()
        self.setup.pack()




class Setup(Frame):

    def __init__(self,master,controller):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        #reference to the master widget, which is the tk window
        self.master = master
        self.init_window()

    def init_window(self):
        self.launch = Button(self,text = "Launch Tracker" ,command =lambda: controller.show_frame(Abilitytracker))
        self.options = Button(self, text = "Options" ,command =lambda: controller.show_frame(options))
        self.setup = Button(self,text = " Setup" , command =lambda: controller.show_frame(Setup))


from tkinter import *
from tkinter import ttk
#from pandas import *
#from numpy import *
import os

# Variables
header2 = ("Calibri", 19)
header3 = ("Calibri", 15)
header4 = ("Calibri", 13)
header5 = ("Calibri", 11)

#Making the basic window structure
window = Tk()
window.title('Get Rich Quick Scam')
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (w, h))
window.configure(background = '#41455C')

class createWindow():
    def __init__(self, window):
        self.window = window
        self.testing = StringVar()
        self.testing.set("Trying")

    def entry_Func(self, whichFrame, varType):
        varNames = {0 : ("longLabel_BuyVstop_TR_Input", "longLabel_BuyVstop_Mult_Input", "longLabel_BuyVstop_WTB_Input"), 1 : ("longLabel_SellVstop_TR_Input", "longLabel_SellVstop_Mult_Input", "longLabel_SellVstop_WTB_Input")}
        varNamesNew = {}
        i = 0
    
        for r in varNames[varType]:
            header = StringVar()
            header.set(r)
            varNamesNew[r] = Entry(whichFrame, bg = "WHITE", textvariable = header)
            varNamesNew[r].config(font = header5, justify = "center")
            varNamesNew[r].place(x= i, y = 99, width = 133)
            i = i + 133
        return varNamesNew
    # def entry_Func(self, whichFrame, varName, i):
    #     varName = Entry(whichFrame, bg = "WHITE", textvariable = self.testing)
    #     varName.config(font = header5, justify = "center")
    #     varName.place(x= i, y = 99, width = 133)


    def run_Window(self):
        # Overall net value frame
        mainCanvas = Canvas(window, bg = '#41455C', width = 1270, height = 9600, bd=0, highlightthickness=0)
        mainCanvas.pack()
        mainLongFrame = Frame(mainCanvas, bg = "GRAY")
        mainLongFrame.place(x = 100, y = 160, width = 399, height = 257)


        #inputLongBuy = self.entry_Func(mainLongFrame, 0)
        inputLongBuy = self.entry_Func(mainLongFrame, 0)
        #longLabel_BuyVstop_TR_Input.config(text = "Something else")

        window.mainloop()


app = createWindow(window)
app.run_Window()
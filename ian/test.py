class createWindow():
    def __init__(self, window):
       self.window = window
       self.testing = StringVar()
       self.testing.set("Trying")

    def entry_Func(self, whichFrame, varName, i):
       varName = Entry(whichFrame, bg = "WHITE", textvariable = self.testing)
       varName.config(font = header5, justify = "center")
       varName.place(x= i, y = 99, width = 133)

    def run_Window(self):
       inputLongBuy = self.entry_Func(mainLongFrame, "longLabel_TR_Input", 0)
       longLabel_TR_Input.config(text = "Something else")
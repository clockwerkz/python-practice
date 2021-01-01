from tkinter import *


def click():
    for i in range(3):
        labelName = "label"+str(i)
        #the tkinker window object as a method "nametowidget" that can grab a widget in the window by it's name:
        targetLabel = window.nametowidget(labelName)
        targetLabel.config(text="New text for label "+str(i), fg="blue", bg="yellow")

def close_window():
    window.destroy()
    exit()

window = Tk()
window.title("Label Change Test")
window.configure(background="black")
Label(window, text="Naming Labels Test", bg="black", fg="white", font="none 12 bold").grid(row=1, column=0, sticky=W)

for i in range(3):
    labelText = "This is label #"+str(i)
    labelName = "label"+str(i)
    #when creating any widget, we can provide a name attribute so we can access it later:
    Label(window, text=labelText,bg="black",fg="white", font="none 12 bold", name=labelName).grid(row=2+i, column=0, sticky=W)

Button(window, text='Change Text Values', width=20, command=click).grid(row=5, column=0, sticky=W)

#exit label
Label(window, text="click to exit", bg="black", fg="white", font="none 12 bold").grid(row=6, column=0, sticky=W)

Button(window, text="Exit", width=14, command=close_window).grid(row=7, column=0, sticky=W)

window.mainloop()


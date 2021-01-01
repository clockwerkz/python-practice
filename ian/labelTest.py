from tkinter import *


def click():
    for i in range(len(labels)):
        labels[i].config(text=str(i)+" Replaced", fg="yellow", bg="green")

def close_window():
    window.destroy()
    exit()

window = Tk()
window.title("Label Change Test")
window.configure(background="black")
labels = []
Label(window, text="Basic Array of Labels Test", bg="black", fg="white", font="none 12 bold").grid(row=1, column=0, sticky=W)

for i in range(3):
    label = "This is label #"+str(i)
    labelPtr = Label(window, text=label,bg="black",fg="white", font="none 12 bold")
    labelPtr.grid(row=2+i, column=0, sticky=W)
    labels.append(labelPtr)

print(labels)
Button(window, text='Change Text Values', width=20, command=click).grid(row=5, column=0, sticky=W)

#exit label
Label(window, text="click to exit", bg="black", fg="white", font="none 12 bold").grid(row=6, column=0, sticky=W)

Button(window, text="Exit", width=14, command=close_window).grid(row=7, column=0, sticky=W)

window.mainloop()


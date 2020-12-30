from tkinter import *

window = Tk()
window.title("My Computer Science Glossary")
window.configure(background="black")
photo1 = PhotoImage(file="circuit.gif")
Label(window, image=photo1, bg="black").grid(row=0, column=0, sticky=W)

window.mainloop()
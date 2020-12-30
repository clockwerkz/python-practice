from tkinter import *

def click():
    entered_text=textentry.get() #this will point to the text element in the window
    output.delete(0.0, END)
    try:
        definition = my_compdictionary[entered_text]
    except:
        definition = "sorry there is no entry for that word in the dictionary"
    output.insert(END, definition)

def close_window():
    window.destroy()
    exit()

window = Tk()
window.title("My Computer Science Glossary")
window.configure(background="black")
photo1 = PhotoImage(file="circuit.gif")

Label(window, image=photo1, bg="black").grid(row=0, column=0, sticky=W)
Label(window, text="Enter the word you would like a definition for:", bg="black", fg="white", font="none 12 bold").grid(row=1, column=0, sticky=W)

textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0, sticky=W)

Button(window, text='SUBMIT', width=6, command=click).grid(row=3, column=0, sticky=W)

Label(window, text="\nDefinition", bg="black", fg="white", font="none 12 bold").grid(row=4, column=0, sticky=W)

output = Text(window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=2, sticky=W)

my_compdictionary = {
    'algorithm':'Step by step instructions to complete a task',
    'bug':'piece of code that causes a program to fail'
}

#exit label
Label(window, text="click to exit", bg="black", fg="white", font="none 12 bold").grid(row=6, column=0, sticky=W)

Button(window, text="Exit", width=14, command=close_window).grid(row=7, column=0, sticky=W)

window.mainloop()
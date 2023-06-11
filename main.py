from tkinter import *

window = Tk()
window.title("Learning Interface")
window.configure(background="red")
window.minsize(150, 300)


def loadWindow1():
    window1 = Toplevel(window)
    window1.title("Learning Interface")
    window1.configure(background="red")
    window1.minsize(200, 300)

    Label(master=window1, text="Welcome " + userInput1.get() + "\nSelect between the following options", bg="red",
          fg="white", font="Apple-Chancery 30").grid(row=0, column=0)
    Label(master=window1, text="", bg="red").grid(row=2, column=0)
    Button(master=window1, text="Mathematics", bg="red", fg="white", font="Apple-Chancery 20").grid(row=3, column=0)
    Label(master=window1, text="", bg="red").grid(row=4, column=0)
    Button(master=window1, text="Physics", bg="red", fg="white", font="Apple-Chancery 20").grid(row=5, column=0)


Label(master=window, text="Please enter your name", padx=150, pady=10, bg="red", fg="white",
      font="Apple-Chancery 30 bold").grid(row=0, column=0)
userInput1 = Entry(master=window, bg="grey", fg="black", font="Apple-Chancery 25")
userInput1.grid(row=1, column=0)
Label(master=window, text="", bg="red").grid(row=3, column=0)
Button(master=window, text="Next", bg="red", fg="white", font="Apple-Chancery 10", command=loadWindow1).grid(row=4,
                                                                                                             column=0)

window.mainloop()

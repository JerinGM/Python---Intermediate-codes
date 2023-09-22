from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.minsize(100, 100)
window.config(padx=70, pady=70)

labelOne = Label(text="Miles")
labelTwo = Label(text="is equal to")
labelThree = Label(text="Km")
labelFour = Label(text="0")
labelOne.grid(column=2, row=0)
labelTwo.grid(column=0, row=1)
labelThree.grid(column=2, row=1)
labelFour.grid(column=1, row=1)

def action():
    user_input = int(entry.get())
    milesToKM = int(user_input * 1.6)
    labelFour.config(text=(f"{milesToKM}"))


button = Button(text="Calculate", command=action)

button.grid(column=1, row=2)

entry = Entry(width=10)
entry.grid(column=1, row=0)











window.mainloop()
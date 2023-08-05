from tkinter import *

window = Tk()
window.title("my first gui program")
window.minsize(width=500, height=300)
window.config(padx=10, pady= 10)

my_label = Label(text="i am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label["text"] = "New Text"
my_label.config(text="New Text")

#button
def button_clicked():
    print("I got clicked")
    n = input.get()
    return my_label.config(text=n)

button = Button(text="click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="new button", command=button_clicked)
new_button.grid(column=3, row=0)

#entry

input = Entry()
input.grid(column=4, row=4)


# grid, place, pack you cant mix them up

window.mainloop()
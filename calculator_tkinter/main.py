from tkinter import *


window = Tk()
window.title("Calculator")
window.minsize(width=400, height=400)
window.config(padx=50, pady=50)



typing_view = Entry(width=20)
typing_view.grid(column=5, row=1)
add = Button(text="+", width=3, height=3)
add.grid(column=5, row=2)
minus = Button(text="-", width=3, height=3)
minus.grid(column=6, row=2)
multiply = Button(text="*", width=3, height=3)
multiply.grid(column=5, row=3)
divide = Button(text="÷", width=3, height=3)
divide.grid(column=6, row=3)
equal = Button(text="=", width=3, height=3)
equal.grid(column=5,row=4,columnspan=2)
# one = Button(text="1", width=3, height=3, command=one)
# one.grid(column=0, row=1)
# two = Button(text="2", width=3, height=3, command=two)
# two.grid(column=1, row=1)
# three = Button(text="3", width=3, height=3, command=three)
# three.grid(column=2, row=1)
# four = Button(text="4", width=3, height=3, command=four)
# four.grid(column=0, row=2)
# five = Button(text="5", width=3, height=3, command=five)
# five.grid(column=1, row=2)
# six = Button(text="6", width=3, height=3, command=six)
# six.grid(column=2, row=2)
# seven = Button(text="7", width=3, height=3, command=seven)
# seven.grid(column=0, row=3)
# eight = Button(text="8", width=3, height=3, command=eight)
# eight.grid(column=1, row=3)
# nine = Button(text="9", width=3, height=3, command=nine)
# nine.grid(column=2, row=3)
# zero = Button(text="0", width=3, height=3, command=zero)
# zero.grid(column=1, row=4)






window.mainloop()

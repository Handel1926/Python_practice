from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=400)
window.config(padx=100, pady=100)

miles = Entry()
miles.grid(column=2, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=3, row=1)

result_label = Label(text="Is equal to")
result_label.grid(column=0, row=2)
result_label.config(padx=10)

result = Label(text="0")
result.grid(column=2, row=2)

km = Label(text="Km")
km.grid(column=3, row=2)

def miles_km():
    m = float(miles.get())
    km = m * 1.609
    result.config(text=km)

calculate = Button(text="Calculate", command=miles_km)
calculate.grid(column=2, row=3)


window.mainloop()
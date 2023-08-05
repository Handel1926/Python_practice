from tkinter import *
number_sign_lists = [["0", "+"]]
number_sign = []
def write_one():
    calc_entry.insert(END, "1")

def write_two():
    calc_entry.insert(END, "2")

def write_three():
    calc_entry.insert(END, "3")
def write_four():
    calc_entry.insert(END, "4")
def write_five():
    calc_entry.insert(END, "5")
def write_six():
    calc_entry.insert(END, "6")
def write_seven():
    calc_entry.insert(END, "7")
def write_eight():
    calc_entry.insert(END, "8")
def write_nine():
    calc_entry.insert(END, "9")
def write_zero():
    calc_entry.insert(END, "0")
def del_by_one():
    numbers_entered = calc_entry.get()
    to_del = len(numbers_entered) - 1
    calc_entry.delete(to_del)
def restart_calc():
    global number_sign_lists
    number_sign_lists = [["0", "+"]]
    calc_entry.delete(0, END)
def add():
    global number_sign, number_sign_lists
    number_sign = [calc_entry.get(), "+"]
    if number_sign[0] == "":
        number_sign_lists = number_sign_lists
        rest = number_sign_lists[0][0]
        result_label.config(text=rest)
    else:
        number_sign_lists.append(number_sign)
        print(number_sign_lists)
        calc_entry.delete(0, END)
        calc_answer()
def subtract():
    global number_sign, number_sign_lists
    number_sign = [calc_entry.get(), "-"]
    print(number_sign)
    if number_sign[0] == "":
        number_sign_lists = number_sign_lists
        rest = number_sign_lists[0][0]
        result_label.config(text=rest)
    else:
        number_sign_lists.append(number_sign)
        print(number_sign_lists)
        calc_entry.delete(0, END)
        calc_answer()
def multiply_calc():
    global number_sign, number_sign_lists
    number_sign = [calc_entry.get(), "*"]
    if number_sign[0] == "":
        number_sign_lists = number_sign_lists
        rest = number_sign_lists[0][0]
        result_label.config(text=rest)
    else:
        number_sign_lists.append(number_sign)
        print(number_sign_lists)
        calc_entry.delete(0, END)
        calc_answer()
def divide_calc():
    global number_sign, number_sign_lists
    number_sign = [calc_entry.get(), "/"]
    if number_sign[0] == "":
        number_sign_lists = number_sign_lists
        rest = number_sign_lists[0][0]
        result_label.config(text=rest)
    else:
        number_sign_lists.append(number_sign)
        print(number_sign_lists)
        calc_entry.delete(0, END)
        calc_answer()

def calc_answer():
    global number_sign_lists
    num_a = number_sign_lists[0][0]
    num_b = number_sign_lists[1][0]
    last_sign = number_sign_lists[1][1]
    print(number_sign_lists)
    if len(number_sign_lists) > 1 and number_sign_lists[0][1] == "+":
        result = float(num_a) + float(num_b)

    if len(number_sign_lists) > 1 and number_sign_lists[0][1] == "-":
        result = float(num_a) - float(num_b)
    if len(number_sign_lists) > 1 and number_sign_lists[0][1] == "*":
        result = float(num_a) * float(num_b)
    if len(number_sign_lists) > 1 and  number_sign_lists[0][1] == "/":
        result = float(num_a) / float(num_b)
    result_label.config(text=f"{result}")
    number_sign_lists = [[str(result), last_sign]]
    print(result)
    print(number_sign_lists)


window = Tk()
window.title("Calculator")
window.minsize(width=400, height=400)
window.maxsize(width=400, height=400)


calc_entry = Entry(width=20)
calc_entry.grid(column=0, row=0, columnspan=20)
result_label = Label(text="")
result_label.grid(column=0, row=1, columnspan=20)

#numbers
one = Button(text="1", command=write_one)
one.grid(column=0, row=2)
two = Button(text="2", command=write_two)
two.grid(column=1, row=2)
three = Button(text="3", command=write_three)
three.grid(column=2, row=2)
four = Button(text="4", command=write_four)
four.grid(column=0, row=3)
five = Button(text="5", command=write_five)
five.grid(column=1, row=3)
six = Button(text="6", command=write_six)
six.grid(column=2, row=3)
seven = Button(text="7", command=write_seven)
seven.grid(column=0, row=4)
eight = Button(text="8", command=write_eight)
eight.grid(column=1,row=4)
nine = Button(text="9", command=write_nine)
nine.grid(column=2, row=4)
zero = Button(text="0", command=write_zero)
zero.grid(column=1,row=4)
plus = Button(text="+", command=add)
plus.grid(column=4, row=2)
minus = Button(text="-", command=subtract)
minus.grid(column=4, row=4)
multiply = Button(text="*", command=multiply_calc)
multiply.grid(column=3, row=3)
divide = Button(text="/", command=divide_calc)
divide.grid(column=5, row=3)
delete = Button(text="delete", command=del_by_one())
delete.grid(column=6, row=2)
restart = Button(text="Restart", command=restart_calc)
restart.grid(column=6, row=5)

window.mainloop()

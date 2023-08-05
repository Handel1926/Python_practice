from tkinter import Label
number = ""





def one():
    global number
    number += "1"


def two():
    global number
    number += "2"



def three():
   number += "3"


def four():
   number += "4"


def five():
    number += "5"


def six():
    number += "6"


def seven():
    number += "7"


def eight():
    number += "8"


def nine():
    number += "9"



def zero():
    number += "0"

typing_view = Label(text=number, width=6, height=1)
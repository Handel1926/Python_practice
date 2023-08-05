from tkinter import *

list_tic = ["o"]

window = Tk()
window.title("Tic Tac Toe")
window.config(padx=50, pady=20)

def reset_button():
    global list_tic
    one_entry.delete(0, END)
    two_entry.delete(0, END)
    three_entry.delete(0, END)
    four_entry.delete(0, END)
    five_entry.delete(0, END)
    six_entry.delete(0, END)
    seven_entry.delete(0, END)
    eight_entry.delete(0, END)
    nine_entry.delete(0, END)
    winner.config(text="player_x, player_o")
    print(list_tic)
def check_game():
    if len(one_entry.get()) == 1 and len(three_entry.get()) == 1 and len(two_entry.get()) == 1:
        if one_entry.get() == two_entry.get() and one_entry.get() == three_entry.get():
            winner_p = one_entry.get()
            return winner.config(text=f"Player {winner_p} is the winner")
    if len(five_entry.get()) == 1 and len(four_entry.get()) == 1 and len(six_entry.get()) == 1:
        if four_entry.get() == five_entry.get() and four_entry.get() == six_entry.get():
            winner_p = one_entry.get()
            return winner.config(text=f"Player {winner_p} is the winner")
    if len(seven_entry.get()) == 1 and len(eight_entry.get()) == 1 and len(nine_entry.get()) == 1:
        if seven_entry.get() == eight_entry.get() and seven_entry.get() == nine_entry.get():
            winner_p = one_entry.get()
            return winner.config(text=f"Player {winner_p} is the winner")
    if len(one_entry.get()) == 1 and len(four_entry.get()) == 1 and len(seven_entry.get()) == 1:
        if one_entry.get() == four_entry.get() and one_entry.get() == seven_entry.get():
            winner_p = one_entry.get()
            return winner.config(text=f"Player {winner_p} is the winner")
    if len(two_entry.get()) == 1 and len(five_entry.get()) == 1 and len(eight_entry.get()) == 1:
        if two_entry.get() == five_entry.get() and two_entry.get() == eight_entry.get():
            winner_p = one_entry.get()
            return winner.config(text=f"Player {winner_p} is the winner")
    if len(three_entry.get()) == 1:
        if three_entry.get() == six_entry.get() and three_entry.get() == nine_entry.get():
            winner_p = one_entry.get()
            return winner.config(text=f"Player {winner_p} is the winner")
    if len(one_entry.get()) == 1 and len(five_entry.get()) == 1:
        if one_entry.get() == five_entry.get() and one_entry.get() == nine_entry.get():
            winner_p = one_entry.get()
            return winner.config(text=f"Player {winner_p} is the winner")
    if len(three_entry.get()) == 1 and len(five_entry.get()) == 1:
        if three_entry.get() == five_entry.get() and three_entry.get() == seven_entry.get():
            winner_p = one_entry.get()
            return winner.config(text=f"Player {winner_p} is the winner\n please hit the rest button")


def one_button():
    global list_tic
    current_player = "x"
    if len(one_entry.get()) == 1:
        pass
    else:
        if list_tic[-1] == "x":
            current_player = "o"
        list_tic.append(current_player)
        one_entry.insert(0, current_player)
        return current_player, check_game()


def two_button():
    global list_tic
    current_player = "x"
    if len(two_entry.get()) == 1:
        pass
    else:
        if list_tic[-1] == "x":
            current_player = "o"
        list_tic.append(current_player)
        two_entry.insert(0, current_player)
        return current_player, check_game()


def three_button():
    global list_tic
    current_player = "x"
    if len(three_entry.get()) == 1:
        pass
    else:
        if list_tic[-1] == "x":
            current_player = "o"
        list_tic.append(current_player)
        three_entry.insert(0, current_player)
        return current_player, check_game()


def four_button():
    global list_tic
    current_player = "x"
    if len(four_entry.get()) == 1:
        pass
    else:
        if list_tic[-1] == "x":
            current_player = "o"
        list_tic.append(current_player)
        four_entry.insert(0, current_player)
        return current_player, check_game()


def five_button():
    global list_tic
    current_player = "x"
    if len(five_entry.get()) == 1:
        pass
    else:
        if list_tic[-1] == "x":
            current_player = "o"
        list_tic.append(current_player)
        five_entry.insert(0, current_player)
        return current_player, check_game()


def six_button():
    global list_tic
    current_player = "x"
    if len(six_entry.get()) == 1:
        pass
    else:
        if list_tic[-1] == "x":
            current_player = "o"
        list_tic.append(current_player)
        six_entry.insert(0, current_player)
        return current_player, check_game()


def seven_button():
    global list_tic
    current_player = "x"
    if len(seven_entry.get()) == 1:
        pass
    else:
        if list_tic[-1] == "x":
            current_player = "o"
        list_tic.append(current_player)
        seven_entry.insert(0, current_player)
        return current_player, check_game()


def eight_button():
    global list_tic
    current_player = "x"
    if len(eight_entry.get()) == 1:
        pass
    else:
        if list_tic[-1] == "x":
            current_player = "o"
        list_tic.append(current_player)
        eight_entry.insert(0, current_player)
        return current_player, check_game()


def nine_button():
    global list_tic
    current_player = "x"
    if len(nine_entry.get()) == 1:
        pass
    else:
        if list_tic[-1] == "x":
            current_player = "o"
        list_tic.append(current_player)
        nine_entry.insert(0, current_player)
        return current_player, check_game()


one_entry = Entry(width=4)
one_entry.grid(column=0, row=0, padx=20, pady=20)
one_button = Button(text='x/o', command=one_button)
one_button.grid(column=0, row=1, padx=20, pady=20)
two_entry = Entry(width=4)
two_entry.grid(column=1, row=0, padx=20, pady=20)
two_button = Button(text='x/o', command=two_button)
two_button.grid(column=1, row=1, padx=20, pady=20)
three_entry = Entry(width=4)
three_entry.grid(column=2, row=0, padx=20, pady=20)
three_button = Button(text='x/o', command=three_button)
three_button.grid(column=2, row=1, padx=20, pady=20)
four_entry = Entry(width=4)
four_entry.grid(column=0, row=2, padx=20, pady=20)
four_button = Button(text='x/o', command=four_button)
four_button.grid(column=0, row=3, padx=20, pady=20)
five_entry = Entry(width=4)
five_entry.grid(column=1, row=2, padx=20, pady=20)
five_button = Button(text='x/o', command=five_button)
five_button.grid(column=1, row=3, padx=20, pady=20)
six_entry = Entry(width=4)
six_entry.grid(column=2, row=2, padx=20, pady=20)
six_button = Button(text='x/o', command=six_button)
six_button.grid(column=2, row=3, padx=20, pady=20)
seven_entry = Entry(width=4)
seven_entry.grid(column=0, row=4, padx=20, pady=20)
seven_button = Button(text='x/o', command=seven_button)
seven_button.grid(column=0, row=5, padx=20, pady=20)
eight_entry = Entry(width=4)
eight_entry.grid(column=1, row=4, padx=20, pady=20)
eight_button = Button(text='x/o', command=eight_button)
eight_button.grid(column=1, row=5, padx=20, pady=20)
nine_entry = Entry(width=4)
nine_entry.grid(column=2, row=4, padx=20, pady=20)
nine_button = Button(text='x/o', command=nine_button)
nine_button.grid(column=2, row=5, padx=20, pady=20)
winner = Label(text="play")
winner.grid(column=0, row=6, columnspan=3, padx=20)
reset = Button(text="reset", command=reset_button)
reset.grid(column=0, row=7)


window.mainloop()

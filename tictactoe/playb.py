class Playb:
    def __init__(self):
        self.list = ["o"]

    def one_button(self):
        current_player = "x"
        if self.list[-1] == "x":
            current_player = "o"
        self.list.append(current_player)
        one_entry.insert(0, current_player)
        return current_player

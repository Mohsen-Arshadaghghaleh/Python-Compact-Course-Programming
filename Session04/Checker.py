class Checker:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col
        self.king = False

    def symbol(self):
        if self.color == "white":
            if self.king:
                return "W"
            else:
                return "w"
        else:
            if self.king:
                return "B"
            else:
                return "b"
from Checker import Checker

class Board:
    def __init__(self):
        self.cells = []
        for x in range(8):
            self.cells.append([None] * 8)
        self.setup()

    def setup(self):
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.cells[row][col] = Checker("black", row, col)

        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.cells[row][col] = Checker("white", row, col)

    def inside(self, row, col):
        if 0 <= row < 8:
            if 0 <= col < 8:
                return True
        return False

    def display(self):
        print("0 1 2 3 4 5 6 7")
        for row in range(8):
            line = []
            for col in range(8):
                checker = self.cells[row][col]
                line.append(checker.symbol() if checker else ".")
            print(row, " ".join(line))

    def legal_moves(self, color):
        moves = []
        captures = []

        for row in range(8):
            for col in range(8):
                checker = self.cells[row][col]
                if checker is None or checker.color != color:
                    continue

                directions = [-1, 1] if checker.king else (
                    [-1] if color == "white" else [1]
                )

                for dr in directions:
                    for dc in (-1, 1):
                        new_row = row + dr
                        new_col = col + dc

                        if self.inside(new_row, new_col) and self.cells[new_row][new_col] is None:
                            moves.append((row, col, new_row, new_col))

                        jump_row = row + 2 * dr
                        jump_col = col + 2 * dc
                        if self.inside(jump_row, jump_col) and self.cells[jump_row][jump_col] is None:
                            middle = self.cells[new_row][new_col] if self.inside(new_row, new_col) else None
                            if middle and middle.color != color:
                                captures.append((row, col, jump_row, jump_col))

        return captures if captures else moves

    def move(self, move):
        row, col, new_row, new_col = move
        checker = self.cells[row][col]
        captured = abs(new_row - row) == 2

        self.cells[new_row][new_col] = checker
        self.cells[row][col] = None
        checker.row = new_row
        checker.col = new_col

        if captured:
            self.cells[(row + new_row) // 2][(col + new_col) // 2] = None

        if checker.color == "white" and new_row == 0:
            checker.king = True
        elif checker.color == "black" and new_row == 7:
            checker.king = True
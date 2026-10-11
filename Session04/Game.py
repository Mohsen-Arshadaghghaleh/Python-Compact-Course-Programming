import time
from Player import Player
from Board import Board


class Game:
    def __init__(self):
        name1 = input("Player 1 name (white): ")
        name2 = input("Player 2 name (black): ")
        self.players = [
            Player(name1, "white"),
            Player(name2, "black")
        ]
        self.board = Board()
        self.moves = 0
        self.start_time = time.monotonic()

    def play(self):
        current = 0

        while True:
            player = self.players[current]
            legal_moves = self.board.legal_moves(player.color)

            if not legal_moves:
                winner = self.players[1 - current]
                break

            print(f"\n{player.name}'s turn ({player.color})")
            self.board.display()
            print("Legal moves:")
            for number, move in enumerate(legal_moves, 1):
                print(number, move)

            choice = input("Enter move number, or F to finish: ").strip()

            if choice.lower() == "f":
                winner = None
                break

            if not choice.isdigit() or not 1 <= int(choice) <= len(legal_moves):
                print("Invalid choice.")
                continue

            self.board.move(legal_moves[int(choice) - 1])
            player.moves += 1
            self.moves += 1
            current = 1 - current

        elapsed = time.monotonic() - self.start_time

        for player in self.players:
            player.time_seconds = elapsed
            if winner is None:
                player.result = "Stopped"
            elif player is winner:
                player.result = "Won"
            else:
                player.result = "Lost"

        print("\nFinal board:")
        self.board.display()
        print("\nGame summary:")
        print(f"Total moves: {self.moves}")
        print(f"Game time: {elapsed:.1f} seconds")
        for player in self.players:
            print(
                f"{player.name}: color={player.color}, moves={player.moves}, "
                f"result={player.result}, time={player.time_seconds:.1f} seconds"
            )


if __name__ == "__main__":
    Game().play()

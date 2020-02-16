class Game:
    def __init__(self, player_one, player_two, N=3):
        self.board = [list(range(i * N + 1, (i + 1) * N + 1)) for i in range(N)]

    def run(self):
         

    def idx_to_coord(self, idx):
        pass

    def display_board(self):
        print(" | ".join([str(x) for x in self.board[0]]))
        for row in self.board[1:]:
            print("---" * len(self.board))
            print(" | ".join([str(x) for x in row]))

    def display():
        pass

    def winnerFound(self, i, j):
        pass

if __name__ == "__main__":
    player_one = input()
    player_two = input()
    game = Game(player_one, player_two)
    game.run()

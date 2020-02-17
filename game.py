class Game:
    def __init__(self, player_one, player_two, N=3):
        self.board = [list(range(i * N + 1, (i + 1) * N + 1)) for i in range(N)]

    def run(self):
        curr_player = 1
        N = len(self.board)
        for i in range(N ** 2):
            curr_player_name = player_one if curr_player == 1 else player_two
            curr_marker = 'x' if curr_player == 1 else 'o'

            self.display_board()
            print("%s, choose a box to place an '%s' into:" % (curr_player_name, curr_marker))
            
            while True:
                idx = Util.get_int_input(lambda x: x.isdigit() and int(x) in range(1, N ** 2 + 1), "Error! box must be an integer and box >= 1 and box <= %s. Input box again:" % N ** 2)
                i, j = self.idx_to_coord(idx)
                if i >= 0 and i < N and j >= 0 and j < N and self.board[i][j] == idx:
                    break
                print("Error! box already taken. Input box again:")

            self.board[i][j] = curr_marker
            if self.winnerFound(i, j):
                self.display_board()
                print("Congratulations %s! You have won." % (curr_player_name))
                return
            curr_player = 1 if curr_player == 2 else 2
        print("Game Ended in a tie")

    def idx_to_coord(self, idx):
        N = len(self.board)
        i = (idx - 1) // N
        j = idx - (i * N) - 1
        return i, j


    def display_board(self):
        print("")
        for i, row in enumerate(self.board):
            row_str = " | ".join([str(x) for x in self.board[i]])
            print(row_str)
            if i != len(self.board) - 1:
                print("-" * len(row_str))
        print("")

    def hasStreak(self, marker, coordRange):
        N = len(self.board)
        streak = 0
        for (y, x) in coordRange:
            if y < 0 or y >= N or x < 0 or x >= N or self.board[y][x] != marker:
                streak = 0
            else:
                streak += 1
                if streak >= 3:
                    return True
        return False

    def winnerFound(self, i, j):
        marker = self.board[i][j]
        streak = 0

        coordRanges = [
            [(i + a, j) for a in range(-2, 3)],         # Vertival
            [(i, j + a) for a in range(-2, 3)],         # Horizontal
            [(i + a, j + a) for a in range(-2, 3)],     # Diagonal down
            [(i - a, j + a) for a in range(-2, 3)]      # Diagonal Up
        ]

        for coordRange in coordRanges:
            if self.hasStreak(marker, coordRange):
                return True
        return False

class Util:
    @staticmethod
    def get_int_input(constraint, errMsg):
        x = ""
        repeat = False
        while not constraint(x):
            if repeat:
                print(errMsg)
            x = input()
            repeat = True
        return int(x)

if __name__ == "__main__":
    print("Enter name for Player 1:")
    player_one = input()
    print("Enter name for Player 2:")
    player_two = input()
    print("Enter N for the N x N tic tac toe game:")
    N = Util.get_int_input(lambda x: x.isdigit() and int(x) >= 3, "Error! N must be an integer and N >= 3. Input N again:")

    game = Game(player_one, player_two, N)
    game.run()

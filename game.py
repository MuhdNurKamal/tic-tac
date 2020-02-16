class Game:
    def __init__(self, player_one, player_two, N=3):
        self.board = [list(range(i * N + 1, (i + 1) * N + 1)) for i in range(N)]

    def run(self):
        curr_player = 1
        for i in range(len(self.board) ** 2):
            curr_player_name = player_one if curr_player == 1 else player_two
            curr_marker = 'x' if curr_player == 1 else 'o'

            self.display_board()
            print("%s, choose a box to place an '%s' into:" % (curr_player_name, curr_marker))
            
            i, j = self.idx_to_coord(int(input()))
            self.board[i][j] = curr_marker
            if self.winnerFound(i, j):
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
        print(" | ".join([str(x) for x in self.board[0]]))
        for row in self.board[1:]:
            print("---" * len(self.board))
            print(" | ".join([str(x) for x in row]))
        print("")

    def winnerFound(self, i, j):
        pass

if __name__ == "__main__":
    print("Enter name for Player 1:")
    player_one = input()
    print("Enter name for Player 2:")
    player_two = input()
    print("Enter N for the N x N tic tac toe game:")
    N = int(input())

    game = Game(player_one, player_two, N)
    game.run()

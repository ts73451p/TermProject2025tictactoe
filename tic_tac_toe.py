class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9          
        self.current_player = "X"       
        self.turn_count = 0 

    def print_board(self):
        print()
        print(self.board[0], "|", self.board[1], "|", self.board[2])
        print("--+---+--")
        print(self.board[3], "|", self.board[4], "|", self.board[5])
        print("--+---+--")
        print(self.board[6], "|", self.board[7], "|", self.board[8])
        print()

    def player_move(self):
        while True:                     # loop
            try:
                move = int(input(
                    f"Player {self.current_player}, choose a position (1-9): "
                ))

                # input validation
                if move < 1 or move > 9:
                    print("Error: Please enter a number between 1 and 9.")
                elif self.board[move - 1] != " ":  # math operation (-)
                    print("Error: That position is already taken.")
                else:
                    self.board[move - 1] = self.current_player
                    break

            except ValueError:
                print("Error: Invalid input. Please enter a number.")

    def check_winner(self):
        win_patterns = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
            (0, 4, 8), (2, 4, 6)               # diagonals
        ]

        for a, b, c in win_patterns:           # loop
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return True

        return False
    
    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def play_game(self):
        print("Welcome to Tic Tac Toe!")
        self.print_board()

        while True:
            self.player_move()
            self.print_board()

            self.turn_count += 1               # math operation (+)

            if self.check_winner():
                print(f"Player {self.current_player} wins!")
                break

            if self.turn_count % 9 == 0:       # math operation (%)
                print("It's a tie!")
                break

            self.switch_player()

    def reset_game(self):
        self.board = [" "] * 9
        self.current_player = "X"
        self.turn_count = 0

def main():
    game = TicTacToe()                          # class instance

    while True:
        game.play_game()
        again = input("Play again? (y/n): ").lower()

        if again != "y":
            print("Thanks for playing!")
            break

        game.reset_game()



main()

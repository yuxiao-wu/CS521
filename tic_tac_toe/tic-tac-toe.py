# File name: tic-tac-toe.py
# Created by: Yuxiao Wu
# Created on : 10/2/2021
# no collaborators, no late days
# source: textbook, wiki
"""
Tic Tac Toe Simulation Starter Code
"""
import random


class TicTacToeSim:

    # Part 1
    def __init__(self):
        # Initialize the simulation
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.AI = False
        self.turn = 1
        self.AITurn = 1

    # Set up board as a 2D list, turn to player 1, and ai to false

    def change_turn(self):
        # Change turn to other player
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1
        return

    def play_game(self):
        # This is the driver method for the simulation
        self.AI = input("Would you like to play against an AI? True/False: ")
        # Play with AI
        if self.AI == "True":
            self.turn = int(input("Would you like to be player 1 or 2? 1/2: "))
            print("Player 1 goes first.")
            if self.turn == 1:
                self.AITurn = 2
                while self.check_winner() == 0:
                    # Player move first
                    self.take_turn(self.turn)
                    self.print_board()
                    if self.check_winner() != 0:
                        break
                    # AI move
                    print("It is Player", self.AITurn, "'s turn.")
                    self.make_move(self.smart_move(), self.AITurn)
                    self.print_board()
            elif self.turn == 2:
                self.AITurn = 1
                while self.check_winner() == 0:
                    # AI moves first
                    print("It is Player", self.AITurn, "'s turn.")
                    self.make_move(self.smart_move(), self.AITurn)
                    self.print_board()
                    if self.check_winner() != 0:
                        break
                    # then player move
                    self.take_turn(self.turn)
                    self.print_board()
        # Play without AI
        else:
            # Keep checking if someone has won
            print("Player", self.turn, "goes first.")
            while self.check_winner() == 0:
                self.take_turn(self.turn)
                self.print_board()
                self.change_turn()
        # Print the player who won or draw
        if self.check_winner() == -1:
            print("It is a draw!")
        elif self.check_winner() == 1:
            print("Player 1 wins!")
        elif self.check_winner() == 2:
            print("Player 2 wins!")
        return

    # Part 2
    def print_board(self):
        # Print the state of the board using X (player 1) and O (player 2)
        for each_row in self.board:
            print("[", end="")
            # Convert the board into readable version
            for each_ele in each_row[0:2]:
                if each_ele == 0:
                    print("' ',", end="")
                elif each_ele == 1:
                    print("'X',", end="")
                else:
                    print("'O',", end="")
            if each_row[2] == 0:
                print("' '", end="")
            elif each_row[2] == 1:
                print("'X'", end="")
            else:
                print("'O'", end="")
            print("]")
        return

    # Part 3
    def get_move(self):
        # Get input from user asking for their move as a tuple
        print("What move would you like to make?")
        row = int(input("Row: "))
        col = int(input("Col: "))
        return row, col

    # Part 4
    def take_turn(self, player):
        # This is the driver method for a players turn
        print("It is Player", player, "'s turn.")
        row, col = self.get_move()
        # check if the move is valid
        while row > 2 or col > 2 or self.board[row][col] != 0:
            print("This move is invalid!")
            row, col = self.get_move()
        self.make_move((row, col), player)
        return

    def get_available_squares(self):
        # Get a list of available squares as tuples (row,col)
        available_squares = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == 0:
                    available_squares.append((row, col))

        return available_squares

    def make_move(self, move, player):
        # Update the board
        self.board[move[0]][move[1]] = player
        return

    # Part 5
    def check_winner(self):
        # Check if a player has won, there are 8 ways to win.
        # Return the player who won 0 if nobody has won, and -1 if it is a draw
        result = -1
        # check for draw
        for row in self.board:
            for ele in row:
                if ele == 0:
                    result = 0
        # check for the same row
        for row in self.board:
            if row[0] == row[1] == row[2] == 1:
                result = 1
            if row[0] == row[1] == row[2] == 2:
                result = 2
        # check for the same column
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == 1:
                result = 1
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == 2:
                result = 2
        # check for the diagonal
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == 1:
            result = 1
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == 2:
            result = 2
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == 1:
            result = 1
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == 2:
            result = 2

        return result

    # Part 6
    def random_move(self):
        # Choose a random move from available moves
        move = random.choice(self.get_available_squares())
        return move

    # Part 7
    def winning_move(self, player):
        # Find a winning move for a player
        move = False
        for i in range(len(self.board)):
            # check for horizontal
            if self.board[i][0] == self.board[i][1] == player and self.board[i][2] == 0:
                move = (i, 2)
            if self.board[i][0] == self.board[i][2] == player and self.board[i][1] == 0:
                move = (i, 1)
            if self.board[i][1] == self.board[i][2] == player and self.board[i][0] == 0:
                move = (i, 0)
            # check for vertical
            if self.board[0][i] == self.board[1][i] == player and self.board[2][i] == 0:
                move = (2, i)
            if self.board[0][i] == self.board[2][i] == player and self.board[1][i] == 0:
                move = (1, i)
            if self.board[1][i] == self.board[2][i] == player and self.board[2][i] == 0:
                move = (0, i)
        # check for diagonal
        if (self.board[0][0] == self.board[2][2] == player or self.board[0][2] == self.board[2][0] == player) and self.board[1][1] == 0:
            move = (1, 1)
        if self.board[0][0] == self.board[1][1] == player and self.board[2][2] == 0:
            move = (2, 2)
        if self.board[2][2] == self.board[1][1] == player and self.board[0][0] == 0:
            move = (0, 0)
        if self.board[0][2] == self.board[1][1] == player and self.board[2][0] == 0:
            move = (2, 0)
        if self.board[1][1] == self.board[2][0] == player and self.board[0][2] == 0:
            move = (0, 2)
        return move

    def threat_to_lose(self):
        # Run winning_move from other perspective
        move = False
        if self.turn == 1:
            move = self.winning_move(2)
        elif self.turn == 2:
            move = self.winning_move(1)
        return move

    def smart_move(self):
        # If there is a winning move, win
        if self.winning_move(self.AITurn):
            move = self.winning_move(self.AITurn)
        # If there is a threat to lose, block
        elif self.threat_to_lose():
            move = self.threat_to_lose()
        # Make random move
        else:
            move = self.random_move()
        return move


# sim = TicTacToeSim()
# sim.play_game()

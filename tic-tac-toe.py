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
        self.AI = eval(input("Would you like to play against an AI? True/False: "))
        self.turn = int(input("Would you like to be player 1 or 2? 1/2: "))
        print("Player", self.turn, "goes first.")
        # Play with AI
        if self.AI:
            while sim.check_winner() == 0:
                # Player move
                self.take_turn(self.turn)
                self.print_board()
                self.change_turn()
                if sim.check_winner() != 0:
                    break
                # AI move
                print("It is Player", self.turn, "'s turn.")
                self.make_move(self.random_move(), self.turn)
                self.print_board()
                self.change_turn()
        # Play without AI
        else:
            # Keep checking if someone has won
            while sim.check_winner() == 0:
                self.take_turn(self.turn)
                self.print_board()
                self.change_turn()
        # Print the player who won or draw
        if sim.check_winner() == -1:
            print("It is a draw!")
        elif sim.check_winner() == 1:
            print("Player 1 wins!")
        elif sim.check_winner() == 2:
            print("Player 2 wins!")
        return

    # Part 2
    def print_board(self):
        # Print the state of the board using X (player 1) and O (player 2)
        for each_row in self.board:
            print("[", end="")
            # Convert the board into readable version
            for each_move in each_row[0:2]:
                if each_move == 0:
                    print("' ',", end="")
                elif each_move == 1:
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
        while self.board[row][col] != 0:
            print("This move is invalid!")
            row, col = self.get_move()
        self.make_move((row, col), player)
        return

    def get_available_squares(self):
        # Get a list of available squares as tuples (row,col)
        available_squares = []
        for row in range(3):
            for col in range(3):
                if sim.board[row][col] == 0:
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
        for row in sim.board:
            for ele in row:
                if ele == 0:
                    result = 0
        # check for the same row
        for row in sim.board:
            if row[0] == row[1] == row[2] == 1:
                result = 1
            if row[0] == row[1] == row[2] == 2:
                result = 2
        # check for the same column
        for i in range(3):
            if sim.board[0][i] == sim.board[1][i] == sim.board[2][i] == 1:
                result = 1
            if sim.board[0][i] == sim.board[1][i] == sim.board[2][i] == 2:
                result = 2
        # check for the diagonal
        if sim.board[0][0] == sim.board[1][1] == sim.board[2][2] == 1:
            result = 1
        if sim.board[0][0] == sim.board[1][1] == sim.board[2][2] == 2:
            result = 2
        if sim.board[0][2] == sim.board[1][1] == sim.board[2][0] == 1:
            result = 1
        if sim.board[0][2] == sim.board[1][1] == sim.board[2][0] == 2:
            result = 2

        return result

    # Part 6
    def random_move(self):
        # Choose a random move from available moves
        move = random.choice(sim.get_available_squares())
        return move

    # Part 7
    def winning_move(self, player):
        # Find a winning move for a player
        return None

    def threat_to_lose(self):
        # Run winning_move from other perspective
        return

    def smart_move(self):
        # If there is a winning move, win
        # If there is a threat to lose, block
        # Make random move
        return


sim = TicTacToeSim()
sim.play_game()

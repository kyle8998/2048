"""
My 2048 command line implementation

Author: Kyle Lim
"""

class Direction:
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0 for y in range(self.width)] for x in range(self.height)]

    def get(self, row, col):
        return self.board[row][col]

    def set(self, row, col, value):
        self.board[row][col] = value

import random
class Game2048:

    def __init__(self, size):
        self.board = Board(size, size)
        # Starting board has two random 2s
        self.generate()
        self.generate()
        self.score = 0

    def render(self):
        print("score:", self.score)
        print("-" * (self.board.width * 8 + 1))
        for row in range(self.board.height):
            for col in range(self.board.width):
                if self.board.get(row, col) is not None:
                    print("|", end=' ')
                    print("{0:5d}".format(self.board.get(row, col)), end=' ')
            print("|")
            print("-" * (self.board.width * 8 + 1))

    def get_move_input(self):
        user_input = input()
        if user_input == "w":
            return Direction.UP
        elif user_input == "a":
            return Direction.LEFT
        elif user_input == "s":
            return Direction.DOWN
        elif user_input == "d":
            return Direction.RIGHT
        else:
            print("Invalid input!")
            return self.get_move_input()

    def lose(self):
        print("You lose! Your score was: "+str(self.score))
        exit()

    def play(self):
        while True:
            self.render()
            if not self.validate():
                self.lose()
            direction = self.get_move_input()
            if not self.slide(direction):
                print("Invalid move, try a different direction!")
            else:
                self.generate()

    def validate(self):
        """
        This is to check if there is any valid moves
        """
        for row in range(len(self.board.board)):
            for col in range(len(self.board.board[0])):
                if self.board.board[row][col] == 0:
                    return True

        for row in range(len(self.board.board)):
            for col in range(1, len(self.board.board[0])):
                if self.board.board[row][col] == self.board.board[row][col-1]:
                    return True

        for col in range(len(self.board.board[0])):
            for row in range(1, len(self.board.board)):
                if self.board.board[row][col] == self.board.board[row-1][col]:
                    return True

        return False


    def slide(self, direction):
        valid = False
        if direction == Direction.UP:
            for row in range(1, len(self.board.board)):
                for col in range(len(self.board.board[0])):
                    i = 1
                    # Determines how far you can move
                    while row-i > 0 and self.board.board[row-i][col] == 0:
                        i += 1

                    if self.board.board[row-i][col] == self.board.board[row][col]:
                        # If a change is made
                        if self.board.board[row][col] != 0:
                            valid = True
                        self.board.board[row-i][col] *= 2
                        self.score += self.board.board[row-i][col]
                        self.board.board[row][col] = 0
                    elif self.board.board[row-i][col] == 0:
                        if self.board.board[row][col] != 0:
                            valid = True
                        self.board.board[row-i][col] = self.board.board[row][col]
                        self.board.board[row][col] = 0
                    else:
                        if row-i+1 != row:
                            if self.board.board[row][col] != 0:
                                valid = True
                            self.board.board[row-i+1][col] = self.board.board[row][col]
                            self.board.board[row][col] = 0

        elif direction == Direction.DOWN:
            for row in range(len(self.board.board)-2, -1, -1):
                for col in range(len(self.board.board[0])):

                    i = 1
                    # Determines how far you can move
                    while row+i < len(self.board.board)-1 and self.board.board[row+i][col] == 0:
                        i += 1

                    if self.board.board[row+i][col] == self.board.board[row][col]:
                        if self.board.board[row][col] != 0:
                            valid = True
                        self.board.board[row+i][col] *= 2
                        self.score += self.board.board[row+i][col]
                        self.board.board[row][col] = 0
                    elif self.board.board[row+i][col] == 0:
                        if self.board.board[row][col] != 0:
                            valid = True
                        self.board.board[row+i][col] = self.board.board[row][col]
                        self.board.board[row][col] = 0
                    else:
                        if row+i-1 != row:
                            if self.board.board[row][col] != 0:
                                valid = True
                            self.board.board[row+i-1][col] = self.board.board[row][col]
                            self.board.board[row][col] = 0

        elif direction == Direction.LEFT:
            for col in range(1, len(self.board.board[0])):
                for row in range(len(self.board.board)):
                    i = 1
                    # Determines how far you can move
                    while col-i > 0 and self.board.board[row][col-i] == 0:
                        i += 1

                    if self.board.board[row][col-i] == self.board.board[row][col]:
                        if self.board.board[row][col] != 0:
                            valid = True
                        self.board.board[row][col-i] *= 2
                        self.score += self.board.board[row][col-i]
                        self.board.board[row][col] = 0
                    elif self.board.board[row][col-i] == 0:
                        if self.board.board[row][col] != 0:
                            valid = True
                        self.board.board[row][col-i] = self.board.board[row][col]
                        self.board.board[row][col] = 0
                    else:
                        if col-i+1 != col:
                            if self.board.board[row][col] != 0:
                                valid = True
                            self.board.board[row][col-i+1] = self.board.board[row][col]
                            self.board.board[row][col] = 0

        elif direction == Direction.RIGHT:
            for col in range(len(self.board.board[0])-2, -1, -1):
                for row in range(len(self.board.board)):
                    i = 1
                    # Determines how far you can move
                    while col+i < len(self.board.board)-1 and self.board.board[row][col+i] == 0:
                        i += 1

                    if self.board.board[row][col+i] == self.board.board[row][col]:
                        if self.board.board[row][col] != 0:
                            valid = True
                        self.board.board[row][col+i] *= 2
                        self.score += self.board.board[row][col+i]
                        self.board.board[row][col] = 0
                    elif self.board.board[row][col+i] == 0:
                        if self.board.board[row][col] != 0:
                            valid = True
                        self.board.board[row][col+i] = self.board.board[row][col]
                        self.board.board[row][col] = 0
                    else:
                        if col+i-1 != col:
                            if self.board.board[row][col] != 0:
                                valid = True
                            self.board.board[row][col+i-1] = self.board.board[row][col]
                            self.board.board[row][col] = 0

        return valid

    def generate(self):
        """
        put random tile in
        """
        possibilities = []
        for row in range(len(self.board.board)):
            for col in range(len(self.board.board[0])):
                if self.board.board[row][col] == 0:
                    possibilities.append((row,col))

        if len(possibilities) == 0:
            # LOSING CONDITION
            self.lose()
        else:
            block = random.randint(0, len(possibilities)-1)
            self.board.board[possibilities[block][0]][possibilities[block][1]] = 2


if __name__ == '__main__':
    print('Choose your board size (4, 5, 6, 7, or 8)')
    # Can definitely clean this up with regex matching, but it's fine
    while True:
        user_input = input()
        if user_input == "" or user_input == "4":
            game2048 = Game2048(4)
            break
        elif user_input == "5":
            game2048 = Game2048(5)
            break
        elif user_input == "6":
            game2048 = Game2048(6)
            break
        elif user_input == "7":
            game2048 = Game2048(7)
            break
        elif user_input == "8":
            game2048 = Game2048(8)
            break
        else:
            print("Enter a valid size 4, 5, 6, 7, or 8")
    game2048.play()
    print()

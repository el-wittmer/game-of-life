"""
Project 2 - Game of Life
Elaina Wittmer
elwittmer
"""

import os

class Life:
    """
    A class to implement Conway's Game of Life
    The game board is represented internally as a list of rows,
    each row itself being a list of Booleans (True == alive)
    """
    
    def __init__(self, width, height, initial_living):
        self.height = height
        self.width = width
        self.living = initial_living
        self.dying = []
        self.board = []
        self.__createBlankBoard()
        self.__updateBoard()

    def alive(self): 
        """ Return a list of (y,x) tuples of current living cells """
        return self.living

    def __str__(self): 
        """ Prints all the symbols in one continuous string"""
        s = ''
        for i in range(len(self.board)):
            row = self.board[i]
            for j in range(len(row)):
                if row[j] == True:
                    s = s + "@"
                else:
                    s = s + "."
        return s
            
    def __call__(self):
        self.__neighbors()

    def show(self): 
        """ Print the current state of the board on screen """
        for i in range(len(self.board)): #loop over the rows of the board, or the width of the board
            row = self.board[i] #go through each cell in the selected row
            for j in range(len(row)):
                if row[j] == True:
                    print ("@", end="")
                else:
                    print(".", end="")
            print("")

    def unshow(self):
        """ Clear the screen """
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def __createBlankBoard(self):
        """Creates a 'beginning' board, which just creates a table of 'False' values"""
        position = False
        for i in range(self.height):
            row = list()
            for j in range(self.width):
                position = False
                row.append(position)   # fill each position in the row with True  
            self.board.append(row)

    def __updateBoard(self):
        """ Loops through the living list getting the x,y values
            and storing True if cell is alive """
        for i in range(len(self.living)):
            xy_pair = self.living[i]
            row = self.board[xy_pair[1]]
            row[xy_pair[0]] = True
            self.board[xy_pair[1]] = row

        for j in range(len(self.dying)):
            xy_pair = self.dying[j]
            row = self.board[xy_pair[1]]
            row[xy_pair[0]] = False
            self.board[xy_pair[1]] = row

    def __neighbors(self):
        grid = self.board
        head_count = 0
        should_live = []
        should_die = []
        alive = False
        head_count = 0

        for j in range(self.width):
            for i in range(self.height):
                top_row = grid[i - 1]

                # top left
                if top_row[j - 1] == True: 
                    head_count += 1

                # top center
                if top_row[j] == True: 
                    head_count += 1

                # top right
                if top_row[(j + 1) % self.width] == True: 
                    head_count += 1

                middle_row = grid[i]

                # middle left
                if middle_row[j - 1] == True: 
                    head_count += 1

                # middle
                if middle_row[j] == True:   
                    alive = True #this is the target cell

                # middle right
                if middle_row[(j + 1) % self.width] == True:    
                    head_count += 1

                bottom_row = grid[(i + 1) % self.height]

                # bottom left
                if bottom_row[j - 1] == True:   
                    head_count += 1

                # bottom middle
                if bottom_row[j] == True:   
                    head_count += 1

                # bottom right
                if bottom_row[(j + 1) % self.width] == True:    
                    head_count += 1

                if alive == True:
                    if head_count < 2:     # dies under-population
                        should_die.append((j,i))

                    elif head_count == 2 or head_count == 3: # lives
                        should_live.append((j,i))

                    else:                            # greater than 3
                        should_die.append((j,i))
                else:
                    if head_count == 3:
                        should_live.append((j,i))

                head_count = 0
                alive = False

        self.living = should_live
        self.dying = should_die
        self.__updateBoard()

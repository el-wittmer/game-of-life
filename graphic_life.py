from graphics import *
from life import *
import os

class GraphicLife(Life):
    def __init__(self, width, height, initial_living):
        super().__init__(width, height, initial_living)
        self.window = GraphWin("Game of Life", self.width * 10, self.height * 10, autoflush = False)

    def show(self):
        self.window.setBackground('white')
        i = 0
        j = 0
        while i < len(self.living):
            cell = self.living[i]
            x = Rectangle(Point(cell[0] * 10 ,cell[1] * 10),Point(cell[0] * 10 + 10, cell[1] * 10 + 10))
            x.setFill('white')
            x.setOutline('white')
            x.draw(self.window)
            background = Rectangle(Point(cell[0] * 10 + 1, cell[1] * 10 + 1), Point(cell[0] * 10 + 7, cell[1] * 10 + 7))
            background.setFill('pink')
            background.setOutline('pink')
            background.draw(self.window)
            petal_one = Oval(Point(cell[0] * 10 + 0, cell[1] * 10 + 3),Point(cell[0] * 10 + 3,cell[1] * 10 + 5))
            petal_one.setFill('orange')
            petal_one.setOutline('orange')
            petal_one.draw(self.window)            
            petal_two = Oval(Point(cell[0] * 10 + 3, cell[1] * 10 + 0),Point(cell[0] * 10 + 5, cell[1] * 10 + 3))
            petal_two.setFill('orange')
            petal_two.setOutline('orange')
            petal_two.draw(self.window)
            petal_three = Oval(Point(cell[0] * 10 + 5,cell[1] * 10 + 3),Point(cell[0] * 10 + 8,cell[1] * 10 + 5))
            petal_three.setFill('orange')
            petal_three.setOutline('orange')
            petal_three.draw(self.window)
            petal_four = Oval(Point(cell[0] * 10 + 3, cell[1] * 10 + 5),Point(cell[0] * 10 + 5,cell[1] * 10 + 8))
            petal_four.setFill('orange')
            petal_four.setOutline('orange')
            petal_four.draw(self.window)
            center = Circle(Point(cell[0] * 10 + 4, cell[1] * 10 + 4), 1)
            center.setFill('cyan')
            center.setOutline('cyan')
            center.draw(self.window)
            i += 1

        while j < len(self.dying):
            blank = self.dying[j]
            x = Rectangle(Point(blank[0] * 10 ,blank[1] * 10),Point(blank[0] * 10 + 9,blank[1] * 10 + 9))
            x.draw(self.window)
            x.setOutline('white')
            x.setFill('white')
            j += 1
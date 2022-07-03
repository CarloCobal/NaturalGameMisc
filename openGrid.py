#opens grid and gathers time and grid data
import pandas as pd
import numpy as np
from timer import endlog, log, getElapsed
from time import perf_counter
import atexit

N = 100
ON = 255
OFF = 0  
vals = [ON, OFF]
lst = []

#open grid csv and load into game
#----------------------------------------------------#
def gridFromCsv(generation=None):
    #unpack np.ndarray from grid.csv
    x = pd.read_csv('grid.csv', header=None)
    #get time from txt file
    with open('oha.txt', 'r') as f:
        time = float(f.read())
    #put x into a np.ndarray
    grid = np.array(x)
    #get the shape of the grid
    shape = grid.shape
    #get the number of rows and columns
    rows = shape[0]
    cols = shape[1]
    return grid

gridFromCsv()

#open txt file and returns the time
#----------------------------------------------------#
def getTime():
    with open('oha.txt', 'r') as f:
        saved_time = float(f.read())
    return saved_time

#opens the updated grid.csv
#----------------------------------------------------#
def adjustGrid():#grid=None): Do in game
    # if grid is None:
    #     grid = np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)
    #     return grid
    # else:
    gridToDelta = gridFromCsv()
    timeToCompare = getTime()
    return gridToDelta, timeToCompare

#obj equiv to gridFromCsv for packaging!!
#----------------------------------------------------#
class Grid:
    def getGrid(self):
        return self.grid
    def getTime(self):
        return self.time

gr1 = Grid()
gr1.grid = gridFromCsv()
print(gr1.grid)
gr1.time = getTime()
print(gr1.time)



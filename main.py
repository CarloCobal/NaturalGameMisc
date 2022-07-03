
#Updates and animates the initial grid
import time as t
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from timer import endlog, log, getElapsed
from time import perf_counter
import atexit
import pandas as pd
from openGrid import gridFromCsv
from openGrid import Grid
from openGrid import getTime
# from timer import getElapsed

N = 100
ON = 255
OFF = 0  
vals = [ON, OFF]
vals2 = [0, 255]
lst = []
ndArr = np.array([])

# populate grid with random on/off - more off than on
# def realRun(gridManifold):
#     gridFromCsv = list
#     if gridFromCsv == True:
#         pass
#     #load grid into game
#     else:
# grid = np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N) #nd.array. To initialize the grid The question is only what grid to init with. 
grid = gridFromCsv() #therefore gridFromCsv is the delta. Chages update grid.csv. 
#     return grid
    
# gridl = gridFromCsv()
# print(variator(gridl))
def update(data):
  startTime = t.time()
  lst = []
  count=0
  global grid

  steadyState = False
  # copy grid since we require 8 neighbors for calculation
  # and we go line by line 
  newGrid = grid.copy()
  for i in range(N):
    for j in range(N):
      # compute 8-neghbor sum 
      # using toroidal boundary conditions - x and y wrap around 
      # so that the simulaton takes place on a toroidal surface.
      total = (grid[i, (j-1)%N] + grid[i, (j+1)%N] + 
               grid[(i-1)%N, j] + grid[(i+1)%N, j] + 
               grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] + 
               grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255
      # apply Conway's rules
      if grid[i, j] == ON:
        if (total < 2) or (total > 3):
          newGrid[i, j] = OFF
          count+=1

        #add noise to grid
        elif np.random.rand() < 0.05:
            newGrid[i, j] = OFF
        
      else:
        if total == 3:
          newGrid[i, j] = ON
          count+=1
    #   if all elements of grid are OFF then we have a steady state
    #   and we can stop the simulation

    # if np.all(newGrid == OFF):
  if count == 0:
    # print("Steady state reached", str((t.time() - startTime)*60),t.time(),startTime)
    # print("--- %s seconds ---" % (t.time() - startTime))
        #stop the animation
    ani.event_source.stop()
    plt.close()

  count=0
        #if no more live cells output the time it took to reach steady state
    
    

#   steadyState = True
  # update data
#   mat.set_data(newGrid)
  #overlay randIP on grid
  mat.set_data(newGrid)#+ np.random.choice(vals, N*N, p=[0.05, 0.95]).reshape(N, N))
  grid = newGrid
  return [mat]

# set up animation
fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, update, interval=50,
                              save_count=50)
plt.show()

start = perf_counter()
newDf= pd.DataFrame(columns=['time', 'data'], index=range(0,1))
# newDf['time'] = start
# newDf['data'] = grid
# newDf.to_csv('/Users/quaidcarlo/Desktop/Crater/PythonCanyon/Conway_Game_Of_Life/Game-of-Life-Haskell/both.csv')
# print(newDf)


#if name is main then run the program
# if __name__ == '__main__':
#   update(grid)
#wait until time is done to compare and send result to ex 
# saved_time = pass
# grid_time = float(endlog())
# if grid_time > save_time:
#     # run findAll

#     print(grid_time)
#     print(save_time)

def grid_delta(grid):
    #iterate grid and find all ON cells
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 255:
                np.append(ndArr, np.random.choice(vals2, p=[0.05, 0.95]))
            if grid[i][j] == 0:
                np.append(ndArr, np.random.choice(vals2, p=[0.05, 0.95]))
    return ndArr

gridA = Grid()
gridA.grid = grid
gridA.time = float(endlog())
print("GRID_A TIME: ", '\n', gridA.time)
print("GRID_A GRID: ", '\n', gridA.grid)

gridB = Grid()
gridB.grid = grid_delta(gridA.grid)
gridB.time = getTime()
print("GRID_B TIME: ", '\n', gridB.time)
print("GRID_B GRID: ", '\n', gridB.grid)
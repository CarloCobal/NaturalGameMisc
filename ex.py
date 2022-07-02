#TODO fix the end timer count error
#TODO fix the animation stop error


#TODO Get max sim time each sim. Select top. Add variation to top. 
import time as t
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from timer import endlog, log, getElapsed
from time import perf_counter
import atexit
import pandas as pd
# from timer import getElapsed

N = 100
ON = 255
OFF = 0  
vals = [ON, OFF]
vals2 = [0, 255]
lst = []

#----------------------------------------------------#
# populate grid with random on/off - more off than on
grid = np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)
#save grid as df
grid_out = pd.DataFrame(grid)
# grid_time = pd.DataFrame(time)
print(grid)
# print(log())
# time_log1 = log()
# print(time_log1) 
#save grid to csv
grid_out.to_csv('/Users/quaidcarlo/Desktop/Crater/PythonCanyon/Conway_Game_Of_Life/Game-of-Life-Haskell/grid.csv')
saved_time1 = float(endlog())
with open('oha.txt', 'w') as f:
    f.write(str(saved_time1))
 
#----------------------------------------------------#
#Open grid from csv
x = pd.read_csv('/Users/quaidcarlo/Desktop/Crater/PythonCanyon/Conway_Game_Of_Life/Game-of-Life-Haskell/grid.csv')
# print(x)
def findall(x):
    for i in range(N):
        for j in range(N):
            if x[i][j] == 255:
                lst.append(np.random.choice(vals2, p=[0.05, 0.95]))

            if x[i][j] == 0:
                lst.append(np.random.choice(vals2, p=[0.95, 0.05]))
        return lst
print(findall(x))
# x.dropna()
#drop the first comma in the grid.csv
x.drop(x.index[0])
arr = np.array(x)
print(arr.shape)
for i in range(N):
    for j in range(N):
        print(arr[i][j], end=" ")
    # print()
print(arr.shape)

def findAll(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 255:
                # lst.append((i,j))
                lst.append(np.random.choice(vals2, p=[0.05, 0.95]))
            if arr[i][j] == 0:
                # lst.append((i,j))
                lst.append(np.random.choice(vals2, p=[0.95, 0.05]))
            else:
                lst.append(arr[i][j])
            
    return lst
print(findAll(arr))
print(len(lst))  #should be 10000


#----------------------------------------------------#
#open txt file and read the time
with open('oha.txt', 'r') as f:
    saved_time1 = float(f.read())
    save_time = saved_time1

# saved_time = pass
grid_time = float(endlog())
if grid_time > save_time:
    # run findAll
    findAll(lst)
    print(grid_time)
    print(save_time)
    #therefore, save time from grid_time and grid2_time
#else run a new random grid for grid 1 
#load same grid into game.
#----------------------------------------------------#
#translate the array list into a grid
reshaped = np.reshape(lst,(200,100))
print(reshaped)


print(float(endlog()))
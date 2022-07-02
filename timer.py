import atexit
from time import perf_counter
from functools import reduce

#only registers stop if plt window is closed
def secondsToStr(t):
    return "%d:%02d:%02d.%03d" % \
        reduce(lambda ll,b : divmod(ll[0],b) + ll[1:],
            [(t*1000,),1000,60,60])

line = "="*40
def log(elapsed=None):
    # print(line)
    # print(secondsToStr(perf_counter()))
    if elapsed:
        print(elapsed)
        # return elapsed
    # print(line)
    # print()

def getElapsed(elapsed=None):
    if elapsed:
        return elapsed
    
    

def endlog():
    end = perf_counter()
    elapsed = end-start
    log(secondsToStr(elapsed))
    return elapsed

def now():
    return secondsToStr(perf_counter())

start = perf_counter()
# atexit.register(endlog)
# log()

# import pandas as pd
# timerLog = pd.DataFrame(columns=['time', 'data'])
# timerLog['time'] = atexit.register(endlog)
# #open grids.csv
# grid = pd.read_csv('/Users/quaidcarlo/Desktop/Crater/PythonCanyon/Conway_Game_Of_Life/Game-of-Life-Haskell/grids.csv')
# print(grid) 
# #set index 
# grid.set_index('Unnamed: 0', inplace=True)
# timerLog['data'] = grid
# print(timerLog)
# #add timerLog to a column in a csv file


#add log to a 
# timerLog.to_csv('/Users/quaidcarlo/Desktop/Crater/PythonCanyon/Conway_Game_Of_Life/Game-of-Life-Haskell/timerLog.csv')
#add log to timerLog

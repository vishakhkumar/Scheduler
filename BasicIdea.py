# just defining reference points so that we don't have to hard code anything in the future.

import math

maximumScale = 10
minimumScale = 1
weightChange = 0.1


class Task(object):
    """A simple implementation of my Task"""

    def __init__(self, a,b,c,d,e,f):

        global weightChange

        self.StartTime    = a
        self.EndTime      = b
        self.Difficulty   = c # optimizing variable
        self.Movability   = d # optimizing variable
        self.Importance   = e
        self.Deadline     = f


    def printInfo(self):
        print("Start Time:" + str(self.StartTime) + " End Time:" + str(self.EndTime))
    def isValid(self, varaaa):
        return True

    def Optimize(self, arr):

        # self.StartTime - the thing we're optimizing.
        # self.EndTime - the thing we are NOT optimizing.

        # doing my silly summation bullshit. Not satanic bullshit, I promise.

        change = 0

        for task in arr:
            change = change + (task.Difficulty + self.Difficulty)/(math.exp(abs(task.EndTime - self.StartTime)))
            change = change - (task.Difficulty + self.Difficulty)/(math.exp(abs(self.EndTime - task.StartTime)))
        # just scaling things down.
        change = change*weightChange # just making my change a nice thing and
        change = (maximumScale - self.Movability)/self.Movability * change
        # just checking
        if self.isValid(change + self.StartTime):
            self.StartTime = self.StartTime + change
            self.EndTime = self.EndTime + change

def OptimizeRun(my_tasks):
    for obj in my_tasks:
        obj.Optimize(my_tasks)
    #print(derivative(funkyMice,3,0.1))

def Main():
    iterations = int(input('Enter the number of iterations : '))
    my_tasks = []
    for i in range(1,5):
        my_tasks.append(Task(10 + i/2 , 10 + i/2 + 0.1,   5,5,i/2,i/2))
    my_tasks.append(Task(0,0.1,10,10,0,0))
    my_tasks.append(Task(23.9,24,10,10,0,0))
    for i in range(iterations):
        OptimizeRun(my_tasks)
    for i in my_tasks:
        i.printInfo()


Main()

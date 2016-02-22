# just defining reference points so that we don't have to hard code anything in the future.

import math

maximumScale = 10
minimumScale = 1
weightChange = 0.1


class Task(object):
    """A simple implementation of my Task"""

    def __init__(self, a,b,c,d,e,f,g):

        global weightChange

        self.StartTime    = float(a)
        self.EndTime      = float(b)
        self.Difficulty   = float(c) # optimizing variable
        self.Movability   = float(d) # optimizing variable
        self.Importance   = float(e)
        self.Deadline     = float(f)
        self.Name         = str(g)

    def __repr__(self):
        return "{}: {} {}".format(self.Name,
                                  self.StartTime,
                                  self.EndTime)
"""
    def Description(self):
        return ( "\n ******************Do not alter these lines******************"
        "\n Name: " + self.Name
        "\n Start Time: " + str(self.StartTime)
        "\n End Time: " + str(self.EndTime)
        "\n Difficulty: " + str(self.Difficulty)
        "\n Movability: " + str(self.Movability)
        "\n Importance: " + str(self.Importance)
        "\n Deadline: " + str(self.Deadline) + "\n")
"""

    def isValid(self, varaaa):
        if self.EndTime < self.Deadline:
            return True
        else:
            return False




    def Optimize(self, arr):

        # self.StartTime - the thing we're optimizing.
        # self.EndTime - the thing we are NOT optimizing.

        # doing my silly summation bullshit. Not satanic stuff, I promise.

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

def getKey(obj):

    return obj.StartTime

def OptimizeRun(my_tasks):
    for obj in my_tasks:
        obj.Optimize(my_tasks)
    #print(derivative(funkyMice,3,0.1))

def Main():

    number = int(input('Enter the number of tasks : '))
    iterations = int(input('Enter the number of iterations : '))
    my_tasks = []

    for i in range(1,number+1):

        print("\n")
        print('Enter the weights of the tasks: ')

        a = float(input('Enter the StartTime: '))
        b = float(input('Enter the EndTime: '))
        c = float(input('Enter the Difficulty: '))
        d = float(input('Enter the Movability: '))
        e = float(input('Enter the Importance: '))
        f = 1000 # leave this for later
        g = str(input('Enter the Name: '))
        my_tasks.append(Task(a,b,c,d,e,f,g))

    # just boundary things
    my_tasks.append(Task(0,0.1,10,10,0,0,'BegDay'))
    my_tasks.append(Task(23.9,24,10,10,0,0,'EndDay'))


    for i in range(iterations):
        OptimizeRun(my_tasks)

    my_tasks = sorted(my_tasks,key=getKey)

    print('\n\n')


#    for i in my_tasks:
#        print(i.Description())


Main()

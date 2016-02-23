# just defining reference points so that we don't have to hard code anything in the future.

import math

maximumScale = 10
minimumScale = 1
weightChange = 0.1


class Task(object):
    """A simple implementation of my Task"""


    def __init__(self,*args):

        global weightChange

        self.Weights = {
        'StartTime'    : float(args[0]),
        'EndTime'      : float(args[1]),
        'Difficulty'   : float(args[2]), # optimizing variable
        'Movability'   : float(args[3]), # optimizing variable
        'Importance'   : float(args[4]),
        'Deadline'     : float(args[5]),
        'Name'         : str(args[6])
        }


    def __repr__(self):
        return "{}: {} {}".format(Weights['Name'],
                                  Weights['StartTime'],
                                  Weights['EndTime'])

    def Description(self):
        return (
        "\n *#****************Do not alter these lines******************"
        "\n *#*Name        : "  + str(self.Weights['Name'])          +
        "\n *#*StartTime   : "  + str(self.Weights['StartTime'])     +
        "\n *#*EndTime     : "  + str(self.Weights['EndTime'])       +
        "\n *#*Difficulty  : "  + str(self.Weights['Difficulty'])    +
        "\n *#*Movability  : "  + str(self.Weights['Movability'])    +
        "\n *#*Importance  : "  + str(self.Weights['Importance'])    +
        "\n *#*Deadline    : "  + str(self.Weights['Deadline'])      +
        "\n *#****************Do not alter these lines******************"+
        "\n")


    def isValid(self, varaaa):
        if self.Weights['EndTime'] < self.Weights['Deadline']:
            return True
        else:
            return False

    def Optimize(self,arr):

        # self.StartTime - the thing we're optimizing.
        # self.EndTime - the thing we are NOT optimizing.
        # doing my silly summation bullshit. Not satanic stuff, I promise.
        change = 0
        for task in arr:
            change = change + (task.Weights['Difficulty'] + self.Weights['Difficulty'])/(math.exp(abs(task.Weights['EndTime'] - self.Weights['StartTime'])))
            change = change - (task.Weights['Difficulty'] + self.Weights['Difficulty'])/(math.exp(abs(self.Weights['EndTime'] - task.Weights['StartTime'])))
        # just scaling things down.
        change = change*weightChange # just making my change a nice thing and
        change = (maximumScale - self.Weights['Movability'])/self.Weights['Movability'] * change
        # just checking
        if self.isValid(change + self.Weights['StartTime']):
            self.Weights['StartTime'] = self.Weights['StartTime'] + change
            self.Weights['EndTime'] = self.Weights['EndTime'] + change

def getKey(obj):

    return obj.Weights['StartTime']

def OptimizeRun(my_tasks):
    for obj in my_tasks:
        obj.Optimize(my_tasks)
    #print(derivative(funkyMice,3,0.1))

def ParseDescription(str):


    releventDescription = [line for line in str.split('\n') if "*#*" in line]
    for line in releventDescription:
        for i in d.keys():
            if i in line
                task(line.split(':')[1])

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

        print("\n")
        my_tasks.append(Task(a,b,c,d,e,f,g))

    # just boundary things
    my_tasks.append(Task(0,0.1,10,10,0,0,'BegDay'))
    my_tasks.append(Task(23.9,24,10,10,0,0,'EndDay'))


    for i in range(iterations):
        OptimizeRun(my_tasks)

    my_tasks = sorted(my_tasks,key=getKey)

    print('\n\n')


    for i in my_tasks:
        print(i.Description())


Main()

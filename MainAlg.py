# just defining reference points so that we don't have to hard code anything in the future.
import math

stringToParse = ( "*#****************Do not alter these lines******************\n"+
 "*#*Name        : EndDay\n"+
 "*#*StartTime   : 23.9\n"+
 "*#*EndTime     : 24.0\n"+
 "*#*Difficulty  : 10.0\n"+
 "*#*Movability  : 10.0\n"+
 "*#*Importance  : 0.0\n"+
 "*#*Deadline    : 0.0\n"+
 "*#****************Do not alter these lines******************\n")

# just scale things.
maximumScale = 10
minimumScale = 1
weightChange = 0.1


class Task(object):
    """A simple implementation of my Task"""
    def __init__(self,vari):
        self.Weights = vari
    def __repr__(self):
        return '{}: {} {}'.format(self.Weights['Name'],self.Weights['StartTime'],self.Weights['EndTime'])
    def Description(self): # creates a description.
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
    def isValid(self, change):
        if self.Weights['EndTime'] + change < self.Weights['Deadline']:
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
        if self.isValid(change):
            self.Weights['StartTime'] = self.Weights['StartTime'] + change
            self.Weights['EndTime'] = self.Weights['EndTime'] + change

def getKey(obj):
    return obj.Weights['StartTime']

def OptimizeRun(my_tasks):
    for obj in my_tasks:
        obj.Optimize(my_tasks)

def ParseDescription(str):  #takes description from Calendar and makes an object from it.

    # just removing unnecessary stuff from the description.
    # This prevents me from reading their stuff as well.
    str = [line for line in str.split('\n') if "*#*" in line]
    # str is a list now

    # just removing all special characters
    b = "# *"
    for j in range( 0 , len(str) ):
        for i in range(0,len(b)):
            str[j] = str[j].replace(b[i],"")

    # str has two useless lines at the beginning and ending.
    # just removing them.
    str = str[1:len(str)-1]
    Name  = [line.split(':')[0] for line in str]
    Value = [line.split(':')[1] for line in str]

    # Creating a Weights for the task
    Weights = {}
    for i in range(0,len(Name)):
        Weights[Name[i]] = Value[i]
    # And now we pass this as a parameter to the Task class.
    #print(Task(Weights).Description())
    #print(Task(Weights))

def defaultWeights(*args):
    Weights = {
    'StartTime'    : float(args[0]),
    'EndTime'      : float(args[1]),
    'Difficulty'   : float(args[2]), # optimizing variable
    'Movability'   : float(args[3]), # optimizing variable
    'Importance'   : float(args[4]),
    'Deadline'     : float(args[5]),
    'Name'         : str(args[6])
            }
    return Weights

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
        my_tasks.append(Task(defaultWeights(a,b,c,d,e,f,g)))

    # just boundary things
    my_tasks.append(Task(defaultWeights(0,0.1,10,10,0,0,'BegDay')))
    my_tasks.append(Task(defaultWeights(23.9,24,10,10,0,0,'EndDay')))


    for i in range(iterations):
        OptimizeRun(my_tasks)

    my_tasks = sorted(my_tasks,key=getKey)

    print('\n\n')


    for i in my_tasks:
        print(i.Description())

#ParseDescription(stringToParse)
Main()

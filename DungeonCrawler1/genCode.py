import random
import math #imported for math.floor to find center of grid

'''
REFERENCES
    (x,y) = int(str(x)+str(y)) READS: xy

TASK LIST
GENERATE A LINKED LIST 
Node code (each node gets procedurely generated) 
    Data in each node is cords = (x,y), rmType = displayed ascii char
List code (maybe put lookup code into it?)
    Use some vector shit to find traversal path.
'''

# node class
class room:
    def __init__(self,cords=None,rmType=None):
        self.cords = cords
        self.rmType = rmType
        self.Nrt = None
        self.Est = None
        self.Sth = None
        self.Wst = None

# linked list class
class map: 
    def __init__ (self,size):
        self.head = room()
        self.size = size
        self.origin = [math.floor(size/2),math.floor(size/2)]
        self.orgIndex = int(str(self.origin[0])+str(self.origin[1]))
        self.lookup = {} # T-or-F table if room at cord is made
        for x in range(size): 
            for y in range(size):
                index = int(str(y)+str(x)) #index of the square in (x,y) form READS: yx
                self.lookup[index] = 'o' #sets isMade status to false
        self.lookup[self.orgIndex] = 1

    '''
    Notes: traverse works but NEEDS comments
    traverse may be unable to backtrack ?
    '''
    def traverse(self, cords, head):
        pathList = [] # the path gets saved here and can be read
        path = [cords[1]-self.origin[1],cords[0]-self.origin[0]] #path[0] = x path[1] = y
        cur = head
        opp = [0,0,0,0] # N E S W
        while (path[0] != 0 or path[1] != 0): #checks if there are no more moves needed
            stepLoopTop = path
            ewLoop = 0 #if these are 2 and theres an entry in opp worry
            nsLoop = 0
            if path[0] == 0 and path[1] == 0:
                break
            if path[0] > 0 or opp[1] == 1: # if the dest is to the east
                opp[1] = 0
                if cur.Est == None:
                    opp[3] = 1
                    ewLoop += 1
                while cur.Est != None:
                    pathList.append([0,1,0,0])
                    cur = cur.Est # move east 1 and update location relative to point
                    path[0] -= 1
            if path[0] < 0 or opp[3] == 1: # if the dest is to the west
                opp[3] = 0
                if cur.Wst == None:
                    opp[1] = 1
                    ewLoop += 1
                while cur.Wst != None:
                    pathList.append([0,0,0,1])
                    cur = cur.Wst # move west 1 and update location relative to point
                    path[0] += 1
            if path[1] > 0 or opp[2] == 1: # if the dest is to the south
                opp[2] = 0
                if cur.Sth == None:
                    opp[0] = 1
                    nsLoop += 1
                while cur.Sth != None:
                    pathList.append([0,0,1,0])
                    cur = cur.Sth # move South 1 and update location relative to point
                    path[1] -= 1
            if path[1] < 0 or opp[0] == 1: # if the dest is to the North
                opp[0] = 0
                if cur.Nrt == None:
                    opp[2] = 1
                    nsLoop += 1
                while cur.Nrt != None:
                    pathList.append([1,0,0,0])
                    cur = cur.Nrt # move North 1 and update location relative to point
                    path[1] += 1
            if stepLoopTop[0] == path[0] and stepLoopTop[1] == path[1]: #hasn't moved
                if cur.Nrt != None:
                    pathList.append([1,0,0,0])
                    cur = cur.Nrt # move North 1 and update location relative to point
                    path[1] += 1
                elif cur.Est != None:
                    pathList.append([0,1,0,0])
                    cur = cur.Est # move east 1 and update location relative to point
                    path[0] -= 1
                elif cur.Sth != None:
                    pathList.append([0,0,1,0])
                    cur = cur.Sth # move South 1 and update location relative to point
                    path[1] -= 1
                elif cur.Wst != None:
                    pathList.append([0,0,0,1])
                    cur = cur.Wst # move west 1 and update location relative to point
                    path[0] += 1
            #print(ewLoop)
            if(ewLoop == 2 and path[0] != 0):
                if(opp[1] == 1 or opp[3] == 1):
                    if (path[0] > 0):
                        pathList.append([0,1,0,0])
                        break
                    if (path[0] < 0):
                        pathList.append([0,0,0,1])
                        break
            if(nsLoop == 2 and path[1] != 0):
                if(opp[0] == 1 or opp[2] == 1):
                    if (path[1] > 0):
                        pathList.append([0,0,1,0])
                        break
                    if (path[1] < 0):
                        pathList.append([1,0,0,0])
                        break
        return pathList

    def append(self,cords,rmType = None):
        print("new path")
        new_room = room(cords,rmType)
        cur = self.head
        nextDir = [0,0,0,0]
        path = self.traverse(cords,cur)
        for step in path:
            #print(step)
            if step[0] == 1:
                print('N')
                if cur.Nrt != None:
                    cur = cur.Nrt
                nextDir = [1,0,0,0]
            elif step[1] == 1:
                print('E')
                if cur.Est != None:
                    cur = cur.Est
                nextDir = [0,1,0,0]
            elif step[2] == 1:
                print('S')
                if cur.Sth != None:
                    cur = cur.Sth
                nextDir = [0,0,1,0]
            elif step[3] == 1:
                print('W')
                if cur.Wst != None:
                    cur = cur.Wst
                nextDir = [0,0,0,1]
        if nextDir[0] == 1:
                cur.Nrt = new_room
        elif nextDir[1] == 1:
                cur.Est = new_room
        elif nextDir[2] == 1:
                cur.Sth = new_room
        elif nextDir[3] == 1:
                cur.Wst = new_room
        self.lookup[int(str(cords[0])+str(cords[1]))] = 1
    
    def printMap(self):
        for x in range(self.size): 
            for y in range(self.size):
                index = int(str(x)+str(y)) #index of the square in (x,y) form READS: xy
                print(f"{self.lookup[index]}",end=" ")
                #print(f"{index}: {self.lookup[index]}",end=" ") #prints for testing
            print()

    #idk how to do this but its worth doing for testing
    # def totalRooms(self):
    #     cur = self.head

    # make a check room function using traverse
        



maptest = map(7)
maptest.printMap()
maptest.append([3,2])
maptest.printMap()
maptest.append([4,2])
maptest.printMap()
maptest.append([4,1])
maptest.printMap()
maptest.append([5,1])
maptest.printMap()
maptest.append([6,1])
maptest.printMap()
maptest.append([6,2]) #only this one seems to be wrong might not be added
maptest.printMap()


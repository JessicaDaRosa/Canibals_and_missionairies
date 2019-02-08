from Noeud import *
def GraphSearch(debut,boatSize):
    fronteer = list()
    visited = list()
    goal = Object(debut.getSon().reverse(),None)
    fronteer.append (debut) # the first objec in our fronteer is the initial case
    foundIt = False
    while len(fronteer)!= 0 and foundIt == False:
        father = fronteer.pop()
        temp = father.Expanse(boatSize)
        for i in range (len(temp)):
            if temp[i] == goal:
                goal = temp[i]
                foundIt = True
            else:
                if fronteer.count(temp[i]) == 0 and visited.count(temp[i]) == 0:
                    fronteer.insert(0, temp[i])
        visited.append(father)
    toReturn = list()
    if goal.getFather()!=None:
        toReturn.append(goal)
        temp = goal
        while temp.getFather()!=None:
            toReturn.insert(0,temp.getFather())
            temp=temp.getFather()
    return toReturn
        # expanse objec (at rhe end)
        # remove it from fronteer
        # add it to visited
        # verify if the expanded content exists in fronteer or is allready expanded or if it's our goal.
        # if none of the above add to fronteer 

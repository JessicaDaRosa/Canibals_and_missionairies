from Noeud import *
def GraphSearch(debut,boatSize):
    fronteer = list()
    visited = list()
    goal = debut.getSon().reverse()
    fronteer.append (debut) # the first objec in our fronteer is the initial case
    foundIt=False
    while foundIt==False:
        temp = fronteer[0].Expanse(boatSize)
        print("\n\t\t>> fronteer[0] << {}".format(len(fronteer)))
        print(fronteer[0])
        for i in range (len(temp)):
            if temp[i] == goal:
                goal = temp[i]
                foundIt = True
            else:
                if fronteer.count(temp[i])==0 and visited.count(temp[i])==0:
                    fronteer.append(temp[i])
        visited.append(fronteer.pop(0))
        print(foundIt)
    return goal
        # expanse objec (position 0)
        # remove it from fronteer
        # add it to visited
        # verify if the expanded content exists in fronteer or is allready expanded or if it's our goal.
        # if none of the above add to fronteer 

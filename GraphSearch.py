from Noeud import *
def GraphSearch(debut,boatSize):
    fronteer = []
    visited = []
    goal = debut.reverse()
    start = Object(debut,None)
    fronteer.append (start) # the first objec in our fronteer is the initial case
    while len(fronteer != 0):
        temp = fronteer.pop(0).Expanse()
        # expanse objec
        # remove it from fronteer
        # add it to visited
        # verify if the expanded content exists in fronteer or is allready expanded or if it's our goal.
        # if none of the above add to fronteer 

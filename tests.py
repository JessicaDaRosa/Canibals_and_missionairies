from State import *
from Noeud import *
from GraphSearch import *
numberOfCannibals = 3
numberOfMissionairies = 3
boatSize = 2
start = Object(State(numberOfCannibals,numberOfMissionairies,0,0,True), None)
temp=GraphSearch(start,2)
for i in range(len(temp)):
    print(temp[i])
    if(i+1!=len(temp)):
        print("______Next______")

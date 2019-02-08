from State import *
class Object :
    # the means to have linked objects in my fronteer 
    # so that in the end I can easly return a solution
    def __init__(self,element, next):
        self.son = element
        self.father = next
    # the inportant thing is th son (State) 
    # so that is what is printed for every object
    def __str__(self):
        if (self.son.boat==True):
            return ("Boat on the Left.\nLeft [C={};M={}] \nRight[C={};M={}]\nPassage number: {}".format(self.son.cL,self.son.mL,self.son.cR,self.son.mR,self.son.cost))
        else:
            return ("Boat on the Right.\nLeft [C={};M={}] \nRight[C={};M={}]\nPassage number: {}".format(self.son.cL,self.son.mL,self.son.cR,self.son.mR,self.son.cost))
    # returns the state from witch this one was generated
    def getFather(self):
        return self.father
    # just returns the current state 
    def getSon(self):
        return self.son
    # generates every estate that is acheavable from the 
    # currente one by generating a list with every movment
    # possible (te list returned is coposed of objects with self as a parent)
    def Expanse(self,boatSize):
        father = self.getSon() # the state that is being expansed 
        temp = State(0,0,0,0,True) # memory allocation 
        results = [] 
        #boat full of canibals
        temp = father.MnC(boatSize)
        if temp != None and temp.test() :
            results.append( Object(temp,self) )
        #boat full of Missionairies
        print("___Father___")
        print(father)
        temp = father.MnM(boatSize)
        print("-->> MnM <<--")
        print(type(temp))
        print(temp)
        if temp != None and temp.test() :
            results.append( Object(temp,self) )
        # the boat must be even numbered for this passage to work properlly
        # half and half 
        print("___Father___")
        print(father)
        temp = father.MCM(int(boatSize/2))
        print("-->> McM <<--")
        print(type(temp))
        print(temp)
        if temp != None and temp.test():
            results.append( Object (temp,self))
        return results
    def __eq__(self, other):
        if type(self)== type(other):
            return self.son == other.son
        else:return False
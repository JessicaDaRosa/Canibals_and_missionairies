from State import *
class Object :
    def __init__(self,element, next):
        self.son = element
        self.father = next
    def __str__(self):
        print (self.son)
    def getFather(self):
        return self.father
    def getSon(self):
        return self.son
    def Expanse(self,boatSize):
        father = self.getSon()
        temp = State(0,0,0,0,True)
        results = []
        #boat full of canibals
        temp = father.MnC(boatSize)
        if temp.test() :
            results.append( Object(temp,self) )
        #boat full of Missionairies
        temp = father.MnM(boatSize)
        if temp.test() : 
            results.append( Object(temp,self) )
        #the boat must be even numbered for this passage to work properlly
        #half and half 
        temp = father.MCM(int(boatSize/2))
        if temp.test() :
            results.append( Object (temp,self))
        return results


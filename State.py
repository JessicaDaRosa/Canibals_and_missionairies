#True = Left
#False = Right
class State :
    def __init__(self, cLeft,mLeft,cRight,mRight,b):
        self.cR = cRight
        self.mR = mRight
        self.cL = cLeft
        self.mL = mLeft
        self.boat = b
        self.cost = 0
    #the state in question will become a copy of the one guiven as an entry
    def copy(self, thing):
        self.cL=thing.cL
        self.cR=thing.cR
        self.mL=thing.mL
        self.mR=thing.mR
        self.boat=thing.boat
        self.cost=thing.cost          
    # simple test to see if the number of cannibals exceeds the number of missionairies
    # True if the state is complycent whith the norms (number of canibals <= numer of missionairies)
    def test (self): 
        #right
        if self.mL == 0 and self.cL==0 and self.cR <= self.mR:
            return True
        if self.mR ==0 and self.cR==0 and self.cL<=self.mL:
            return True
        right = False
        if (self.mR == 0 and self.cR!=0) or (self.mR!=0 and self.cR <= self.mR):
            right = True
        #left
        left = False
        if (self.mL == 0 and self.cL != 0) or (self.mL!=0 and self.cL <= self.mL):
            left = True
        return right == left
    # how to print an element
    def __str__(self):
        if (self.boat==True):
            return ("Boat on the Left.\nLeft [C={};M={}] \nRight[C={};M={}]\nPassge number: {}".format(self.cL,self.mL,self.cR,self.mR,self.cost))
        else:
            return ("Boat on the Right.\nLeft [C={};M={}] \nRight[C={};M={}]\nPassge number: {}".format(self.cL,self.mL,self.cR,self.mR,self.cost))
    # comparison of two elements (==) 
    def __eq__(self, other):
     
        if (other != None and self.cR == other.cR):
            if (self.cL == other.cL):
                if (self.mR == other.mR):
                    if (self.mL == other.mL):
                        if self.boat == other.boat :
                            return True
        else:
            return False
    #move n Canibals
    # returns a new instance of State where cannibals where moved
    # return None if the move isn't possible
    def MnC(self,number):
        temp = State (0,0,0,0,True) # memory allocation for our new variable
        temp.copy(self)
        if(temp.boat == True):#Left
            if (temp.cL > 0): # to enshure no negative number of canibals
                temp.boat = False
                if number != 0 : temp.cost = temp.cost+1 
                if(temp.cL >= number): # sone canibals stay a shore
                    temp.cL = temp.cL - number
                    temp.cR = temp.cR + number
                elif temp.cL < number : # no cannibals left on this side
                    temp.cR = temp.cR + temp.cL
                    temp.cL = 0
        elif (temp.boat == False):#Right
            if (temp.cR > 0):
                temp.boat = True
                if number != 0 : temp.cost = temp.cost + 1
                if(temp.cR >= number): # there will be canibals left on the right
                    temp.cR = temp.cR - number
                    temp.cL = temp.cL + number
                if temp.cR < number : #no canibals left on the right
                    temp.cL = temp.cL + temp.cR
                    temp.cR = 0
        # if the criterian aren't met and there is no passage tem will have the value 
        # of the supposed parent and in that case we will return an empty state
        if temp == self : 
            print("MnC srewup")
            return None
        else:
            return temp
    #move n Missionairies
    # returns a new instance of State where Missionairies where moved
    # return None if the move isn't possible
    def MnM(self, number):
        temp = State(0,0,0,0,True)
        temp.copy(self)
        if(temp.boat == True):#Left
            if temp.mL > 0 : # are there missionairies on the shore?
                temp.boat=False # if yes the boat can move
                if number != 0 : temp.cost = temp.cost +1
                if temp.mL >= number: # are there more missionairies than places on the boat?
                    temp.mL = temp.mL - number
                    temp.mR = temp.mR + number
                elif temp . mL < number :# to avoid negatif numbers if we have less missionairis than places (1 missionarie)
                    temp.mR = temp.mR + temp.mL
                    temp.mL = 0                 
        elif temp.boat == False:#Right
            if temp.mR > 0 : # are there missionairies on the shore?
                temp.boat = True # if yes the boat can move
                if number != 0 : temp.cost = temp.cost +1
                if temp.mR >= number : # are there more missionairies than places on the boat?
                    temp.mR = temp.mR - number
                    temp.mL = temp.mL + number
                elif temp.mR < number:# to avoid negatif numbers if we have less missionairis than places (1 missionarie)
                    temp.mL = temp.mL + temp.mR
                    temp.mR = 0
        if temp == self:
            print("MnM srewup")
            return None
        else:
            return temp 
    #nmissionairies and n canibals at the same time
    def MCM(self, number):
        temp = State (0,0,0,0,True)
        temp.copy(self)
        if temp.boat == True:#Left
            if (temp.cL > 0 and temp.mL > 0) :#number of canibals and missionairies is positif
                temp.boat = False
                if number != 0 : temp.cost = temp.cost +1
                if temp.cL >= number: #there are enough canibals
                    if temp.mL >= number:#there are enough missionairies 
                        temp.mL = temp.mL - number
                        temp.cL = temp.cL - number
                        temp.mR = temp.mR + number
                        temp.cR = temp.cR + number
                    elif temp.mL < number:#to avoid negatif numbers
                        temp.cR = temp.cR + number
                        temp.cL = temp.cL - number
                        temp.mR = temp.mR + temp.mL
                        temp.mL = 0
                elif temp.cL < number: #the number of canibals is inferior to the number of places on the boat
                    if temp.mL >= number:
                        temp.mL = temp.mL - number
                        temp.mR = temp.mR + number
                        temp.cR = temp.cR + temp.cL
                        temp.cL = 0
                    if temp.mL < number :
                        temp.mR = temp.mR + temp.mL
                        temp.mL = 0
                        temp.cR = temp.cR + temp.cL
                        temp.cL = 0
        elif temp.boat == False : #Right
            if temp.cR>0 and temp.mR>0: #the number of cannials and missionairies is positif
                temp.boat = True
                if number != 0 : temp.cost = temp.cost +1
                if temp.cR>=number: #there are enought
                   if(temp.mR >= number):
                        temp.mL = temp.mL + number
                        temp.cL = temp.cL + number
                        temp.mR = temp.mR - number
                        temp.cR = temp.cR - number
                   if temp.mR < number :
                        temp.mL = temp.mL + temp.mR
                        temp.mR = 0
                        temp.cL = temp.cL + number
                        temp.cR = temp.cR - number
                elif temp.cR < number : 
                    if temp.mR >= number :
                        temp.mR = temp.mR - number
                        temp.mL = temp.mL + number
                        temp.cL = temp.cL + temp.cR
                        temp.cR = 0
                    if temp.mR < number : 
                        temp.mL = temp.mL + temp.mR
                        temp.mR = 0
                        temp.cL = temp.cL + temp.cR
                        temp.cR = 0
        if temp == self :
            print("MCM srewup")
            return None
        else:
            return temp
    #returns a state where every position is inversed
    def reverse (self):
        if self.boat == False : return State (self.cR,self.mR,self.cL,self.mL,True)
        if self.boat == True : return State (self.cR,self.mR,self.cL,self.mL,False)

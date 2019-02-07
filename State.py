#True = Left
#False = Right
class State :
    def __init__(self, cRight,mRight,cLeft,mLeft,b):
        self.cR = cRight
        self.mR = mRight
        self.cL = cLeft
        self.mL = cRight
        self.boat = b
        self.cost = 0
    #true if numbers are respected
    def copy(self, thing):
        self.cL=thing.cL
        self.cR=thing.cR
        self.mL=thing.mL
        self.mR=thing.mR
        self.boat=thing.boat
        self.cost=thing.cost          
    def test (self): 
        if(self.cR <= self.mR):
            if(self.cL <= self.mL):
                return True
        else:
            return False
    def __str__(self):
        if (self.boat==True):
            return ("Boat on the Left.\nLeft [C={};M={}] \nRight[C={};M={}]\nPassge number: {}\n".format(self.cL,self.mL,self.cR,self.mR,self.cost))
        else:
            return ("Boat on the Right.\nLeft [C={};M={}] \nRight[C={};M={}]\nPassge number: {}\n".format(self.cL,self.mL,self.cR,self.mR,self.cost))
    def __eq__(self, other):
        if (self.cR == other.cR):
            if (self.cL == other.cL):
                if (self.mR == other.mR):
                    if (self.mL == other.mL):
                        if self.boat == other.boat :
                            return True
        else:
            return False
    #move n Canibals
    def MnC(self,number):
        temp = State (0,0,0,0,True)
        temp.copy(self)
        if(temp.boat == True):#Left
            if (temp.cL >0):
                temp.boat = False
                temp.cost = temp.cost+1 
                if(temp.cL >= number):
                    temp.cL = temp.cL - number
                    temp.cR = temp.cR + number
                elif temp.cL < number :
                    temp.cR = temp.cR + temp.cL
                    temp.cR = 0
        elif (temp.boat == False):#Right
            if (temp.cR > 0):
                temp.boat = True
                temp.cost = temp.cost + 1
                if(temp.cR >= number):
                    temp.cR = temp.cR - number
                    temp.cL = temp.cL + number
                if temp.cR < number :
                    temp.cL = temp.cL + temp.cR
                    temp.cR = 0
        if temp == self :
            return None
        else:
            return temp
    #move n Missionairies
    def MnM(self, number):
        temp = State(self.cR,self.mR,self.cL,self.mL,self.boat)
        if(temp.boat == True):#Left
            if temp.mL > 0 :
                temp.boat=False
                if temp.mL >= number:
                    temp.mL = temp.mL - number
                    temp.mR = temp.mR + number
                elif temp . mL < number :#to avoid negatif numbers
                    temp.mR = temp.mR + temp.mL
                    temp.mL = 0                 
        elif temp.boat == False:#Right
            if temp.mR > 0 :
                temp.boat = True
                if temp.mR >= number :
                    temp.mR = temp.mR - number
                    temp.mL = temp.mL + number
                elif temp.mR < number:#to avoid negatif numbers
                    temp.mL = temp.mL + temp.mR
                    temp.mR = 0
        if temp == self:
            return None
        else:
            return temp 
    #nmissionairies and n canibals at the same time
    def MCM(self, number):
        temp = State(self.cR,self.mR,self.cL,self.mL,self.boat)
        if temp.boat == True:#Left
            if (temp.cL > 0 and temp.mL > 0) :#number of canibals and missionairies is positif
                temp.boat = False
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
                if temp.cR>=number: #there are enought
                   if(temp.mR >= number):
                        temp.mL = temp.mL - number
                        temp.cL = temp.cL - number
                        temp.mR = temp.mR + number
                        temp.cR = temp.cR + number
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
            return None
        else:
            return temp
    def reverse (self):
        if self.boat == False : return temp = State (self.cL,self.mL,self.cR,self.mL,True)
        if self.boat == True : return temp = State (self.cL,self.mL,self.cR,self.mL,False)

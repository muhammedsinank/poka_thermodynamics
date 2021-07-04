#simple tool to make analysis on closed system

class closedsystem():
    def __init__(self):
        self.mass=1
        self.P=None
        self.V=None
        self.T=None
        self.Q=None
        self.W=None
    def heat(self,Q):
        #set heat addition in a process(-Q will be for heat rejection)
        self.Q=Q
    def work(self,W):
        #set work done in a process(-W will be for work addition)
        self.W=W
#we need to make a super class named process which will have initial and final states
#and makes use of the closed system class
        
        
        
        
        

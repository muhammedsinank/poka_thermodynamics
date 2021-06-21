import numpy as np

class ideal_gas():
    def __init__(self):
        #initialize properties
        self.pressure=None
        self.volume=None
        self.temprature=None
        self.internal_energy=None
        self.enthalpy=None
        self.entropy=None
        self.R=8.3145
        self.table=[]
        #read in the air data properties and save it to self.data
        with open("ideal_gas_properties_of_air.csv") as f:
            self.table = np.genfromtxt(f,delimiter=",",skip_header=1)
        np.set_printoptions(suppress=True)
    
            
            
    def interpolate(self,idx0,idx1,column,real_value):
        #used to find values in between the values available in the table
        upper_row  = self.table[idx0]   
        lower_row = self.table[idx1]
        btw_val = []  
        
        x0 = real_value  
        x1 = upper_row[column]  
        x2 = lower_row[column]
        for i in range(len(upper_row)):
            if i == 5:                        
                y1 = upper_row[i]
                y2 = lower_row[i]
                y0 = y1 - (abs(y2-y1)/abs(x2-x1)) * abs(x0 -x1) 
                btw_val.append(y0)   
                continue
            y1 = upper_row[i]   
            y2 = lower_row[i]
            y0 = y1 + (abs(y2-y1)/abs(x2-x1)) * abs(x0 -x1)  
            btw_val.append(y0)
        return btw_val

        
    def check_in_between(self,column,var):
         #used to get row above and below in the table if the variable value is not given in the table
        for i in range(len(self.table)):
            if var < self.table[i][column] and column != 5:    
                idx0,idx1 = i-1,i
                interp_val = self.interpolate(idx0,idx1,column,var)
                return interp_val
            elif var > self.table[i][column] and column == 5:  
                idx0,idx1 = i-1,i
                interp_val = self.interpolate(idx0,idx1,column,var)
                return interp_val
                
    def check_in_table(self,column,var):
        #checks if the given value is in the table
        for i in range(1,len(self.table)):
            if self.table[i][column]==var:
                return self.table[i]
            else: return None
            
    def find_row(self,variable,var_value):
        #given a property find in wich row the property belongs in the table
        #if not in the table interpolate to find the values
        column=None
        if variable=="T":
            column=0
        elif variable=="H":
            column=1
        elif variable=="U":
            column=2
        elif variable=="S0":
            column=3
        elif variable=="PR":
            column=4
        elif variable=="VR":
            column=5
        else:
            print("enter a property variable {T,H,U,PR,VR}")
        if column!=None:
            y=self.check_in_table(column,var_value)
            if y!=None:
                return y
            else:
                return self.check_in_between(column,var_value)
                
gas=ideal_gas()
values = gas.find_row("T",325)
print("Property values of air : ",values)
        
        
            
           

        

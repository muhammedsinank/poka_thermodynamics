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
            self.table_duplicate= [line.split() for line in f]
        for i in range(len(self.table_duplicate)):
            self.table_duplicate[i]=self.table_duplicate[i][0].split(",")
        for i in range(1,len(self.table_duplicate)):
            #print(self.table_duplicate[i])
            self.table.append([float(k) for k in self.table_duplicate[i]])
        print(self.table)
            
            
    #def interpolatre(raw_upper,raw_lower,column,real_value):
        #used to find values in between the values available in the table


    

        
    def check_in_between(self,column,var):
        #used to get raw above and below in the table if the variable value is not given in the table
        for i in range(1,len(self.table)):
            if var> self.table[i][column]:
                if var<self.table[i-1][column]:
                    return[self.table[i-1],i]
                else:
                    return[i,self.table[i+1]]
                
    def check_in_table(self,column,var):
        #checks if the given value is in the table
        for i in range(1,len(self.table)):
            if self.table[i][column]==var:
                return self.table[i]
            
    def find_raw(self,variable,var_value):
        #given a property find in wich raw the property belongs in the table
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
                print("bai")
                return self.check_in_between(column,var_value)
                
a=ideal_gas()        
        
        
        
            
           

        

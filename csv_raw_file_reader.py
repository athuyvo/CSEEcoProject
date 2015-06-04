
# coding: utf-8

# In[1]:

#Team Seals
#Heather, Mitchell, Ricky, Anh 
#Reads original CSV data


# In[8]:

import numpy as np


# In[9]:

class RawData(object):
    def __init__ (self, filename):
        self.filename = filename 
        self.headers = None
        self.data = None
    
    def read(self):
        got_header = False 
        for line in open(self.filename, 'r'):
         fields = line.strip().split(",")
         if not got_header:
            self.headers.np.append(fields[0])
            self.headers.np.append(fields[1])
            self.headers.np.append(fields[2]) 
            self.headers.np.append(fields[3])
            self.headers.np.append(fields[4])
            got_header = True
         else: 
            self.data[0].np.append(float(fields[0]))
            self.data[1].np.append(float(fields[1]))
            self.data[2].np.append(float(fields[2]))
            self.data[3].np.append(float(fields[3]))
            self.data[4].np.append(float(fields[4]))
    
    def getParVar(self):
        return self.headers
    
    def GetData(self):
        return self.data
    
    def GetCol(self, ColNum):
        return self.data[:,ColNum]
    
    def DataMatrix(self):
        data = np.genfromtxt('marine_data.csv', delimiter = ',')       
        x = data[1:, 1:]
        matrix = np.matrix([[x[0][0], 0, 0, 0, 0],[x[0][1], x[1][0], 0, 0, 0], [0, x[1][1], x[2][0], 0, 0], [0, 0, x[2][1],x[3][0],0], [0, 0, 0, x[3][1],x[4][0]]])
        BA = np.matrix(x[:, 2])
        tBA = np.transpose(BA)
        BioMass = np.linalg.solve(matrix,tBA)
        print tBA   
        print matrix
        return BioMass
    


# In[10]:

RD = RawData('marine_data.csv')
RD.DataMatrix()


# In[ ]:





# coding: utf-8

# In[ ]:

#Team Seals
#Reads CSV file with new parameters


# In[1]:

import numpy as np


# In[3]:

class NewData(object):
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
        data = np.genfromtxt('marine_data_2.csv', delimiter = ',')       
        x = data[1:, 1:]
        matrix = np.matrix([[x[0][0], 0, 0, 0, 0],[x[0][1], x[1][0], 0, 0, 0], [0, x[1][1], x[2][0], 0, 0], [0, 0, x[2][1],x[3][0],0], [0, 0, 0, x[3][1],x[4][0]]])
        newBA = np.matrix(x[:, 2])
        tnewBA = np.transpose(newBA)
        NewBioMass = np.linalg.solve(matrix,tnewBA)
        #print tnewBA   
        #print matrix
        return NewBioMass

ND = NewData('marine_data_2.csv')
ND.DataMatrix()


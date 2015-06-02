
# coding: utf-8

# In[1]:

#Team Seals
#Heather, Mitchell, Ricky, Anh 


# In[2]:

from numpy import *


# In[3]:

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
            self.headers.append(fields[0])
            self.headers.append(fields[1])
            self.headers.append(fields[2]) 
            self.headers.append(fields[3])
            self.headers.append(fields[4])
            got_header = True
         else: 
            self.data[0].append(float(fields[0]))
            self.data[1].append(float(fields[1]))
            self.data[2].append(float(fields[2]))
            self.data[3].append(float(fields[3]))
            self.data[4].append(float(fields[4]))
    
    def getParVar(self):
        return self.headers
    
    def GetData(self):
        return self.data
    
    def GetCol(self, ColNum):
        return self.data[:,ColNum]
    
    def DataMatrix(self):
        data = genfromtxt('marine_data.csv', delimiter = ',')
        x = data[1:, 1:]
        return x
    


# In[5]:

RD = RawData('marine_data.csv')
RD.DataMatrix()


# In[ ]:




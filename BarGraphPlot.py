
# coding: utf-8

# In[1]:

from csv_raw_file_reader import RawData
from csv_new_file_reader import NewData

import math 
import numpy as np
import matplotlib.pyplot as plt


# In[2]:

x = RawData('marine_data.csv')


# In[3]:

BioMass = x.DataMatrix()
print BioMass


# In[4]:

y = NewData('marine_data_2.csv')


# In[5]:

NewBioMass = y.DataMatrix()
print NewBioMass


# In[6]:

n_groups = 5
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.4
    


# In[7]:

origBiomass = plt.bar(index, BioMass, bar_width,
                 alpha=opacity,
                 color='b',
                 label='BioMass')


# In[8]:

newBiomass = plt.bar(index, NewBioMass, bar_width,
                 alpha=opacity,
                 color='r',
                 label='NewBioMass')


# In[9]:

high = max(BioMass)
low = min(BioMass)
plt.ylim([0, math.ceil(high+0.5*(high-low))])


# In[12]:

Animal_1 = input('Enter first animal in "quotes": ')



# In[ ]:

Animal_2 = input('Enter second animal in "quotes": ')


# In[13]:

Animal_3 = input('Enter third animal in "quotes": ')


# In[15]:

Animal_4 = input('Enter fourth animal in "quotes": ')


# In[16]:

Animal_5 = input('Enter fifth animal in "quotes": ')


# In[17]:

plt.xlabel('Animals')
plt.ylabel('Biomass (kg)')
plt.title('Ecosystem Model: Biomass')
plt.xticks(index + bar_width, (Animal_1, Animal_2, Animal_3, Animal_4, Animal_5))
plt.legend()


# In[ ]:

plt.tight_layout()
plt.show()


# In[ ]:




# In[ ]:




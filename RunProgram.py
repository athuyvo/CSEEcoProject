
from csv_raw_file_reader import RawData
from csv_new_file_reader import NewData

import math 
import numpy as np
import matplotlib.pyplot as plt


x = RawData(filename)


BioMass = x.DataMatrix()
print BioMass


y = NewData(filename2)


NewBioMass = y.DataMatrix()
print NewBioMass


n_groups = 5
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.5
opacity = 0.4
    

origBiomass = plt.bar(index, BioMass, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Biomass')


newBiomass = plt.bar(index, NewBioMass, bar_width+0.25,
                 alpha=opacity,
                 color='g',
                 label='New Biomass')


high = max(BioMass)
low = min(BioMass)
plt.ylim([0, math.ceil(high+0.2*(high-low))])



Animal_1 = input('Enter first animal in "quotes": ')

Animal_2 = input('Enter second animal in "quotes": ')

Animal_3 = input('Enter third animal in "quotes": ')

Animal_4 = input('Enter fourth animal in "quotes": ')

Animal_5 = input('Enter fifth animal in "quotes": ')

plt.xlabel('Species')
plt.ylabel('Biomass (kg)')
plt.title('Ecosystem Model: Biomass')
plt.xticks(index + bar_width, (Animal_1, Animal_2, Animal_3, Animal_4, Animal_5))
plt.legend()

plt.tight_layout()
plt.show()


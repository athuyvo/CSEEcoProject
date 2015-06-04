# -*- coding: utf-8 -*-
"""
Created on Thu Jun 04 09:52:35 2015
@author: Jia Li
CSE 490 - plotting the biomass
"""

from csv_raw_file_reader import RawData
from csv_new_file_reader import NewData

import numpy as np
import matplotlib.pyplot as plt

def plotBiomassData(data):
    initBiomass = RawData.DataMatrix.BioMass
    changedBiomass = NewData.DataMatrix.NewBioMass

    n_groups = 5
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.4
    
    origBiomass = plt.bar(index, initBiomass, bar_width,
                 alpha=opacity,
                 color='b',
                 label='initial data')
            
    newBiomass = plt.bar(index, changedBiomass, bar_width,
                 alpha=opacity,
                 color='r',
                 label='new data')

    plt.xlabel('Animals')
    plt.ylabel('Biomass (kg)')
    plt.title('Ecosystem Model: Biomass')
    plt.xticks(index + bar_width, ('Harbor Seals', 'Pacific Cod', 'Shrimp', 'Microzooplankton', 'Gelatinous Zooplankton'))
    plt.legend()

    plt.tight_layout()
    plt.show()
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 05 12:06:11 2015

@author: Jia Li
"""

from csv_raw_file_reader import RawData
from csv_new_file_reader import NewData

import numpy as np
import matplotlib.pyplot as plt

def plotBiomassData():
    initBiomass = RD.DataMatrix()
    changedBiomass = ND.NewData()
    
    type(initBiomass)
    type(changedBiomass)
    
    
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
    origBiomass
    newBiomass
    plt.xlabel('Animals')
    plt.ylabel('Biomass (kg)')
    plt.title('Ecosystem Model: Biomass')
    plt.xticks(index + bar_width, ('Harbor Seals', 'Pacific Cod', 'Shrimp', 'Microzooplankton', 'Gelatinous Zooplankton'))
    plt.legend()

    plt.tight_layout()
    plt.show()
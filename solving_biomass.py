# -*- coding: utf-8 -*-
"""
Created on Tue Jun 02 15:56:35 2015

@author: JiaLi
"""

from EcoSystemProj import RawData

class SolvingBiomass(object):
    
    def __init__(self, data):
        self.data = data
        self.biomass = None
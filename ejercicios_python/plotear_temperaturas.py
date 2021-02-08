# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 15:29:59 2021

@author: Agustin Podesta
"""

import numpy as np
temperaturas = np.load('Data/Temperaturas.npy')

import matplotlib.pyplot as plt
plt.hist(temperaturas, bins =25)

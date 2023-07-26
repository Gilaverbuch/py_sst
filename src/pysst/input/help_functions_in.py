# -*- coding: utf-8 -*-
"""
Python module to read the .D binary data files

.. module:: help functions for input module functions

:author:
    Gil Averbuch (gil.averbuch@whoi.edu)

:copyright:
    Gil Averbuch

:license:
    This code is distributed under the terms of the
    GNU General Public License, Version 3
    (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import matplotlib.pyplot as plt
plt.rcParams['font.size'] = '16'
plt.rcParams['figure.dpi'] = 125
plt.rcParams['figure.facecolor'] = 'white'


import numpy as np
import pandas as pd



# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

def select_data_(dsx_, date, d_day, n_day, d_hour, n_hour):
    '''
    this function selects data from the SST archive based on the selected time parameters. 
    
    parameters
    ----------
        dsx_: SST archive data.
        date: numpy datetime64 object or array of datetime64 objects
        d_day: day intervals after date
        n_day: number of day intervals 
        d_hour: number of hours following date
        n_hour: number of hour intervals
    

    Returns
    -------
    xarray object
    '''




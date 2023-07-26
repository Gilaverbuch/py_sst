# -*- coding: utf-8 -*-
"""
Python module to read the .D binary data files

.. module:: py sea surface temperature

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



from .input.input import load_data_


def load_data(date, d_day=0, n_day=0, d_hour=0, n_hour=0):
    '''
    this function loads satelite SST data and returns an xarray object with the data. 
    
    parameters
    ----------
        date: numpy datetime64 object or array of datetime64 objects
        d_day: day intervals after date
        n_day: number of day intervals 
        d_hour: number of hours following date
        n_hour: number of hour intervals

    Returns
    -------
    xarray object
    '''

    print(date, d_day, n_day, d_hour, n_hour)

    sst = load_data_(date)

    return sst



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


def load_data(date):
    '''
    this function loads satelite SST data and returns an xarray object with the data. 
    
    parameters
    ----------
        date: numpy datetime64 object or array of datetime64 objects
    

    Returns
    -------
    xarray object
    '''

    print(date)

    dsx = load_data_(date)

    print(dsx)
    
    dsx.mcsst.plot(cmap='gnuplot2', clim=(5,35))



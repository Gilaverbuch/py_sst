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



from .input.input import load_data_, merge_data_


def load_data(date_i, date_f = None, merge = True):
    '''
    this function loads satelite SST data and returns an xarray object with the data. 
    
    parameters
    ----------
        date_i: initial time as numpy datetime64 object or array of datetime64 objects
        date_f: Default is None unless final time is given as numpy datetime64 object or array of datetime64 objects. 
        merge: merge data sets from various sources. Default is True.

    Returns
    -------
    xarray object
    '''
    
    sst = load_data_(date_i, date_f)

    if merge is True:
        sst = merge_data_(sst)

    return sst



class SST(object):
    def __init__(self, date_i = None, date_f = None):

        self.date_i = date_i
        self.date_f = date_f


    def load_data(self):
        '''
        this function loads satelite SST data and returns an xarray object with the data. 
        
        parameters
        ----------
            date_i: initial time as numpy datetime64 object or array of datetime64 objects
            date_f: Default is None unless final time is given as numpy datetime64 object or array of datetime64 objects. 
            merge: merge data sets from various sources. Default is True.

        Returns
        -------
        xarray object
        '''
        
        self.sst = load_data_(self.date_i, self.date_f)

        # if merge is True:
        #     sst = merge_data_(sst)

        # return sst


    def merge(self):
        '''
        this function merges sst data from both datasets 
        
        parameters
        ----------


        Returns
        -------
        xarray object
        '''
        
        self.sst = merge_data_(self.sst)






# -*- coding: utf-8 -*-
"""
Python module to read the .D binary data files

.. module:: input functions

:author:
    Gil Averbuch (gil.averbuch@whoi.edu)

:copyright:
    Gil Averbuch

:license:
    This code is distributed under the terms of the
    GNU General Public License, Version 3
    (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""

import numpy as np
import xarray as xr
import nctoolkit as nc

from .help_functions_in import load_data_mid_atl_
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


def load_data_(date_i, date_f, lat_min, lat_max, lon_min, lon_max, area):
    '''
    this function loads satelite SST data and returns an xarray object with the data. 
    
    parameters
    ----------
        date_i: initial time as numpy datetime64 object or array of datetime64 objects
        date_f: Default is None unless final time is given as numpy datetime64 object or array of datetime64 objects. 
        lat_min: min coordinate. Default is None
        lat_max: max coordinate. Default is None
        lon_min: min coordinate. Default is None
        lon_max: max coordinate. Default is None
        area: area to get data for. Currentlty gets 'mid-atlantic' (1X1 km grid) or 'global' (4X4 km grid) 
    

    Returns
    -------
    xarray object
    '''


    if date_i is not None:

        if area=='mid-atlantic':

            ds_ = load_data_mid_atl_(date_i, date_f, lat_min, lat_max, lon_min, lon_max)

        elif area=='global':

            print('this functionality is not working yet')
            print('please wait a few days...')
            ds_ = None
    

    return ds_


# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


def merge_data_(sst_):
    '''
    this function merges sst data from both datasets
    
    parameters
    ----------
        sst_: array of xarray datasets containing sst data
    

    Returns
    -------
    xarray object
    '''
    if len(sst_) > 1:
        if sst_[0].time.size > 1:
            for t in range(0, sst_[0].time.size):
                sst_temp = sst_[0].isel(time=t).copy()
                a_ = []
                for i in range(0, len(sst_)):
                    a_.append(sst_[i].isel(time=t).mcsst.values)
                temp = np.nanmean(np.dstack((a_)),len(sst_))
                sst_temp.mcsst.values = temp
                
                try:
                    sst_comb = xr.concat([sst_comb,sst_temp], 'time')
                except:
                    sst_comb = sst_temp.copy()
        else:

            sst_comb = sst_[0].copy()
            a_ = []
            for i in range(0, len(sst_)):
                a_.append(sst_[i].mcsst.values)
            temp = np.nanmean(np.dstack((a_)),len(sst_))
            sst_comb.mcsst.values = temp
            




        for i in range(0, len(sst_)):
            name_ = 'mcsst_source'+str(i+1)
            print(name_)
            sst_comb[name_] = sst_[i].mcsst
        
        

    else:
        sst_comb = sst_[0].copy()
    

    return sst_comb






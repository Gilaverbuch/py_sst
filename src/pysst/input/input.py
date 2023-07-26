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
import pandas as pd

import nctoolkit as nc


from .help_functions_in import select_data_
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


def load_data_(date_i, date_f=0):
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

    year = date_i.astype(object).year

    if date_f!=0:
        date_f = np.datetime64(date_f)



    ds1 = nc.open_thredds('http://tds.maracoos.org/thredds/dodsC/AVHRR/'+str(year)+'/1Agg')

    ds2 = nc.open_thredds('http://basin.ceoe.udel.edu/thredds/dodsC/avhrr_unfiltered_sst.nc')

    try:
        dsx1 = ds1.to_xarray()
        dsx1 = dsx1.sortby('time')

        dsx1 = select_data_(dsx1, date, d_day, n_day, d_hour, n_hour)
    except:
        print('first source does not have data for this year')

    try:
        dsx2 = ds2.to_xarray()
        dsx2 = dsx2.sortby('time')
    except:
        print('second source does not have data for this year')


    dsx1 = dsx1.sel(time=date, method='nearest')

    dsx2 = dsx2.sel(time=date, method='nearest')

    dsx = dsx1.copy()
    dsx.mcsst.values = np.nanmean(np.dstack((dsx1.mcsst.values,dsx2.mcsst.values)),2)
    

    return dsx






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


# from .help_functions_in future_func
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


def load_data_(date_i, date_f=None):
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


    ds1 = nc.open_thredds('http://tds.maracoos.org/thredds/dodsC/AVHRR/'+str(year)+'/1Agg')

    ds2 = nc.open_thredds('http://basin.ceoe.udel.edu/thredds/dodsC/avhrr_unfiltered_sst.nc')

    try:
        dsx1 = ds1.to_xarray()
        dsx1 = dsx1.sortby('time')

    except:
        print('first source does not have data for this year')

    try:
        dsx2 = ds2.to_xarray()
        dsx2 = dsx2.sortby('time')
    except:
        print('second source does not have data for this year')



    if date_f is not None:
        print ('Selecting data in time range', date_i, '--', date_f)
        dsx1 = dsx1.sel(time=slice(date_i, date_f))
        dsx2 = dsx2.sel(time=slice(date_i, date_f))
    else:
        print ('Selecting data closest to', date_i)
        dsx1 = dsx1.sel(time=date_i, method='nearest')
        dsx2 = dsx2.sel(time=date_i, method='nearest')


    print('loading first source...')
    dsx1.load()

    print('loading second source...')
    dsx2.load()

    

    return [dsx1, dsx2]


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
        




    
    
    sst_comb = sst_comb.assign(mcsst_source1 = sst_[0].mcsst)
    sst_comb = sst_comb.assign(mcsst_source2 = sst_[1].mcsst)


    

    return sst_comb






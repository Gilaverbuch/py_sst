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


def load_data_(date_i, date_f, lat_min, lat_max, lon_min, lon_max):
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


    if date_i is not None:

        year = date_i.astype(object).year

        ds_ = []

        # First source
        try:
            ds1 = nc.open_thredds('http://tds.maracoos.org/thredds/dodsC/AVHRR/'+str(year)+'/1Agg')
            dsx1 = ds1.to_xarray()
            dsx1 = dsx1.sortby('time')

            ds_.append(dsx1)

        except:
            print('first source does not have data for this year')

        # # Second source
        # if dsx1 is not None:
        #     try:
        #         ds1 = nc.open_thredds('https://tds.maracoos.org/thredds/dodsC/AVHRR.nc')
        #         dsx1 = ds1.to_xarray()
        #         dsx1 = dsx1.sortby('time')

        #         ds_.append(dsx1)

        #     except:
        #         print('second source does not have data for this year')

        # Second source
        try:
            ds2 = nc.open_thredds('http://basin.ceoe.udel.edu/thredds/dodsC/avhrr_unfiltered_sst.nc')
            dsx2 = ds2.to_xarray()
            dsx2 = dsx2.sortby('time')

            ds_.append(dsx2)
        except:
            print('second source does not have data for this year')



        if date_f is not None:
            print ('Selecting data in time range', date_i, '--', date_f)

            for i in range(0,len(ds_)):
                ds_[i] = ds_[i].sel(time=slice(date_i, date_f))

        else:
            print ('Selecting data closest to', date_i)

            for i in range(0,len(ds_)):
                ds_[i] = ds_[i].sel(time=date_i, method='nearest')


        if lat_min is not None and lat_max is not None and lon_min is not None and lon_max is not None:
            print('selecting data in lat-lon coordinate range')

            for i in range(0,len(ds_)):
                ds_[i] = ds_[i].sel(lat=slice(lat_min, lat_max))

            for i in range(0,len(ds_)):
                ds_[i] = ds_[i].sel(lon=slice(lon_min, lon_max))


        else:
            print('One or more of the min/max lat-lon coordinates is missing . Retrieving all...')

        print('loading data....')
        for i in range(0,len(ds_)):
                ds_[i].load()


    else:
        print('Initial date is missing. Please provide date_i')
    

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
            




        
        
        sst_comb = sst_comb.assign(mcsst_source1 = sst_[0].mcsst)
        sst_comb = sst_comb.assign(mcsst_source2 = sst_[1].mcsst)

    else:
        sst_comb = sst_[0].copy()
    

    return sst_comb






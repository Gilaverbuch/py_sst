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


import numpy as np
import xarray as xr
import nctoolkit as nc
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen



# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

def load_data_mid_atl_(date_i, date_f, lat_min, lat_max, lon_min, lon_max):
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
    

    Returns
    -------
    xarray object
    '''

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

    

    return ds_


# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

def load_data_global_(date_i, date_f, lat_min, lat_max, lon_min, lon_max):
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
    

    Returns
    -------
    xarray object
    '''

    year = date_i.astype(object).year
    year = str(year)
    month = date_i.astype(object).month
    if month<10:
        month = '0'+str(month)
    else:
        month = str(month)

    day = date_i.astype(object).day
    if day<10:
        day = '0'+str(day)
    else:
        day = str(day)

    req = Request('https://www.ncei.noaa.gov/thredds-ocean/catalog/pathfinder/Version5.3/L3C/'+year+'/data/catalog.html')
    html_page = urlopen(req)

    soup = BeautifulSoup(html_page, "html.parser")

    links = []
    for link in soup.findAll('a'):
        links.append(link.get('href'))

    day_ = year + month + day

    ds_=[]

    for l in links:
        if (day_ in l) and ('.nc' in l):
            
            path_ = l.split("pathfinder/",1)[1]
            new_path = 'https://www.ncei.noaa.gov/thredds-ocean/dodsC/pathfinder/' + path_
            
            ds1 = nc.open_thredds(new_path)
            dsx1 = ds1.to_xarray()

            ds_.append(dsx1)




    if date_f is not None:
        print ('Selecting data in time range is not working yet for global')

        # for i in range(0,len(ds_)):
        #     ds_[i] = ds_[i].sel(time=slice(date_i, date_f))

    # else:
    #     print ('Selecting data closest to', date_i)

    #     for i in range(0,len(ds_)):
    #         ds_[i] = ds_[i].sel(time=date_i, method='nearest')


    if lat_min is not None and lat_max is not None and lon_min is not None and lon_max is not None:
        print('selecting data in lat-lon coordinate range')

        for i in range(0,len(ds_)):
            ds_[i] = ds_[i].sel(lat=slice(lat_max, lat_min))

        for i in range(0,len(ds_)):
            ds_[i] = ds_[i].sel(lon=slice(lon_min, lon_max))


    else:
        print('One or more of the min/max lat-lon coordinates is missing . Retrieving all...')

    print('loading data....')
    for i in range(0,len(ds_)):
            ds_[i].load()

    

    return ds_

    




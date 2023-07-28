# -*- coding: utf-8 -*-
"""
Python module to read the .D binary data files

.. module:: output functions

:author:
    Gil Averbuch (gil.averbuch@whoi.edu)

:copyright:
    Gil Averbuch

:license:
    This code is distributed under the terms of the
    GNU General Public License, Version 3
    (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""

import xarray as xr
import numpy as np
import os


# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------


def write_to_nc_(sst_, path):
    '''
    Saves data to netCDF file
    
    parameters
    ----------
    sst_: xarray dataset 
    path: path to save the data. 
    
    
    '''

    if sst_.time.size > 1:

        t_i = np.datetime_as_string(sst_['time'].values[0], unit='D')
        t_f = np.datetime_as_string(sst_['time'].values[-1], unit='D')

        f_name = 'Results/'+t_i+'-'+t_f+'.nc'

        if os.path.exists(f_name):

            print('File exist. Deleting old file...')
            os.remove(f_name)

            print('Saving new file...')
            sst_.to_netcdf(path=f_name)


        else:

            print('Saving new file...')
            sst_.to_netcdf(path=f_name)




    else:

        t_i = np.datetime_as_string(sst_['time'].values, unit='D')

        f_name = 'Results/'+t_i+'.nc'

        if os.path.exists(f_name):

            print('File exist. Deleting old file...')
            os.remove(f_name)

            print('Saving new file...')
            sst_.to_netcdf(path=f_name)


        else:

            print('Saving new file...')
            sst_.to_netcdf(path=f_name)





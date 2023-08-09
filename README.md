# pysst
Python tool to download Sea Surface Temperature. 
Mid-Atlantic (1km X 1km) is retrieved from http://basin.ceoe.udel.edu/thredds ,  http://tds.maracoos.org/thredds/ , 
Global data (4kn X 4km) is retrieved from https://www.ncei.noaa.gov/products/avhrr-pathfinder-sst 

In a conda environment run:

- conda install python 

- pip install build (A simple, correct PEP 517 build frontend. It will build the .whl and .tar.gz for the pip install)

For some reason the nctoolkit, cdo, and cartopy are not installed properly via pip install .whl, so please install the separately. 

- pip install nctoolkit==0.9.4

- conda install -c conda-forge cdo

- conda install -c conda-forge cartopy


cd to the package directory and run:

- python -m build

- pip install dist/the_desired_version.whl



Dependencies:

- Numpy
- Matplotlib
- Jupyter Notebook
- Xarray

** pip install should install them automatically.

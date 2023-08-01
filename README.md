# py_sst
Python tool to dowload Sea Surface Temperature. 
For now, it is retrieving data from http://basin.ceoe.udel.edu/thredds and http://tds.maracoos.org/thredds/ .
The spatial cover is [20,52,-100, -50] (lat/lon).

In a conda environment run:

- conda install python 

- pip install build (A simple, correct PEP 517 build frontend. It will build the .whl and .tar.gz for the pip install)

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

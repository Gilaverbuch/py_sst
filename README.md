# pysst
Python tool to download sattelite (AVHRR) Sea Surface Temperature data. 
Mid-Atlantic (1km X 1km) is retrieved from http://basin.ceoe.udel.edu/thredds ,  http://tds.maracoos.org/thredds/ , 
Global data (4km X 4km) is retrieved from https://www.ncei.noaa.gov/products/avhrr-pathfinder-sst 

In terminal run:

- conda env create -f pysst.yml

This command will create the pysst environment. Then run:

- conda activate pysst

cd to the package directory and run:

- python -m build

- pip install dist/the_desired_version.whl



Dependencies:
- python
- numpy
- matplotlib
- jupyter Notebook
- xarray
- build
- nctoolkit
- cdo
- cartopy

* They are all installed in the process described above.

* Contact: gil.averbuch@whoi.edu

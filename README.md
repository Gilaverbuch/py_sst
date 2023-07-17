# py_sst
Python tool to dowload Sea Surface Temperature

In a conda environment run:

- conda install python 

- pip install build (A simple, correct PEP 517 build frontend. It will build the .whl and .tar.gz for the pip install)

cd to the package directory and run:

- python -m build

- pip install dist/the_desired_version.whl

- pip install nctoolkit==0.9.4

- conda install -c conda-forge cdo

- conda install -c conda-forge cartopy


Dependencies:

- Numpy
- Matplotlib
- Jupyter Notebook
- Pandas
- Xarray
- tqdm

** pip install should install them automatically.

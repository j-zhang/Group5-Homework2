Group5-Homework2
================

Preliminary Setup Steps
-----------------------
To run this code you'll need to install the following packages
inside your virtual machine:

    sudo apt-get install libgeos-3.3.3 python-mpltoolkits.basemap python-mpltoolkits.basemap-data python-mpltoolkits.basemap-doc
    sudo apt git install python-pandas

Running Code
-------------

* Clone this repository to your desktop

* Open Virtual Machine and cd into the directory that you want to save the earthquake data to

Then run the notebook from your machine with this command:

    ipython notebook --no-browser --ip=0.0.0.0 --script --pylab=inline

* Open ipython notebook in your browser and import the file 'recent_earthquakes.py' from this repository that you cloned

* Run each code cell to read in live earthquake data

* Run code cell 4 to cache data

* The cached data will be titled "EarthQuakeData" followed by the date

* The cached data will be saved to the directory in which you ran ipython notebook

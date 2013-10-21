# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import urllib
import json
import pandas as pd

url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_week.geojson'
d = json.loads(urllib.urlopen(url).read())

data = pd.DataFrame(d.items())

data

# <codecell>

data[1][1][0]

# <codecell>

earthquakes = []

for fields in data[1][1]:

    src = fields['properties']['net']
    eqid = fields['properties']['code']
    datetime = fields['properties']['time']
    lon = fields['geometry']['coordinates'][0]
    lat = fields['geometry']['coordinates'][1]
    mag = fields['properties']['mag']
    depth = fields['geometry']['coordinates'][2]
    nst = fields['properties']['nst']
    place = fields['properties']['place']
    
    earthquake = []
    earthquake.append(src)
    earthquake.append(eqid)
    earthquake.append(datetime)
    earthquake.append(lat)
    earthquake.append(lon)
    earthquake.append(mag)
    earthquake.append(depth)
    earthquake.append(nst)
    earthquake.append(place)
    earthquakes.append(earthquake)

#earthquakes

df = pd.DataFrame(np.array(earthquakes), columns = ['Src','Eqid','Datetime','Lat','Lon','Mag','Depth','Nst','Place'])
df[0:10]

# <codecell>

#To Cache Data

import datetime

today = datetime.date.today()
today  = str(today)
Name = 'EarthQuakeData' + today + '.txt'

df.to_csv(Name)

# <codecell>

california = df[df.Src=='ci']
california[0:5]
print california.Lon[0:5]
california.Lat[0:5]

# <codecell>

from mpl_toolkits.basemap import Basemap

def plot_quakes(quakes):
    m = Basemap(llcrnrlon=min(quakes.Lon),llcrnrlat=min(quakes.Lat),
                urcrnrlon=max(quakes.Lon),urcrnrlat=max(quakes.Lat),
                resolution='l',area_thresh=1000.,projection='merc',
                lat_0=62.9540,lon_0=-149.2697)
    m.drawcoastlines()
    m.drawcountries()
    m.fillcontinents(color='coral',lake_color='blue')
    m.drawmapboundary(fill_color='aqua')
    
   # for lon, lat, mag in zip(quakes.Lon, quakes.Lat, quakes.Magnitude):
        #x,y=m(lon,lat)
        #msize = mag * 10
        #m.plot(x, y, markersize = msize)
    x, y = m(quakes.Lon, quakes.Lat) 
    m.plot(x, y, 'k.')
    return m

plot_quakes(alaska)



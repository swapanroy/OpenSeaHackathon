
 #from owslib.wfs import WebFeatureService
#wfs = WebFeatureService(url='https://geo.vliz.be/geoserver/Emodnetbio/wfs', version='2.0.0')

from owslib.wms import WebMapService
import xml.etree.ElementTree as ET 
import pandas as pd 
import os


wms = WebMapService('https://ec.oceanbrowser.net/emodnet/Python/web/wms', version='1.3.0')

#Chlorophyll Index
#https://ec.oceanbrowser.net/emodnet/Python/web/wms?SERVICE=WMS&REQUEST=GetCapabilities&VERSION=1.3.0

#print(list(wms.contents)) #list all available datasets
dataset = wms['By_sea_regions/Baltic_Sea/Water_body_chlorophyll-a.4Danl.nc*Water body chlorophyll-a_L2']

print(dataset.boundingBoxWGS84)
print([op.name for op in wms.operations])
print(wms.getOperationByName('GetMap').methods)
print(wms.getOperationByName('GetMap').formatOptions)
print(dataset.crsOptions)
print(dataset.styles)
print("Dimensions",list(dataset.dimensions)) #Get's time and Elevation 

#Print time and Elevation value
for keys,values in dataset.dimensions.items():
    print(keys)
    print(values)



img = wms.getmap(   layers=['By_sea_regions/Baltic_Sea/Water_body_chlorophyll-a.4Danl.nc*Water body chlorophyll-a_L2'],
                    styles=['contourf'],
                    srs='EPSG:4326',
                    bbox=(9.4, 30.9, 53, 65.9),
                    size=(300, 300),
                    time=('spring 2015'),
                    format='image/png',
                    transparent=True
                    )
#out = open('spring_1982_chlorophyll_Baltic_Sea', 'wb')
out = open('spring_2015_chlorophyll_Baltic_Sea.png', 'wb')
out.write(img.read())
out.close()
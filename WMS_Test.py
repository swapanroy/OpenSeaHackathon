
 #from owslib.wfs import WebFeatureService
#wfs = WebFeatureService(url='https://geo.vliz.be/geoserver/Emodnetbio/wfs', version='2.0.0')

from owslib.wms import WebMapService
import requests
from PIL import Image
from io import BytesIO
import xml.etree.ElementTree as ET 
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
print("Dimensions",list(dataset.dimensions)) #Get's time and 

# Pull legend url from the wms
url = dataset.styles['pcolor_flat']['legend']

 
response = requests.get(url)
m = Image.open(BytesIO(response.content))   # convert to image 
m.save('output.png') 




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
                    transparent=True,
                    legend= "http://ec.oceanbrowser.net/emodnet/Python/web/wms?request=GetLegendGraphic;service=WMS;version=1.3.0;width=100;height=300;format=image/png;layer=By_sea_regions/Baltic_Sea/Water_body_chlorophyll-a.4Danl.nc%2AWater%20body%20chlorophyll-a_L2;style=contour;label=mg/m3"
                )
#out = open('spring_1982_chlorophyll_Baltic_Sea', 'wb')
#out = open('spring_1995_chlorophyll_Baltic_Sea.png', 'wb')


out = open('spring_2015_chlorophyll_Baltic_Sea.png', 'wb')
out.write(img.read())
out.close()

# Lay an image over another 
body = Image.open("output.png")
newsize = (100,180)
body = body.resize(newsize)
body2 = Image.open("spring_2015_chlorophyll_Baltic_Sea.png")

#positioning of the legend on the actual image
body2.paste(body, (210,120))
body2.save("spring_2015_chlorophyll_Baltic_Sea_final.png")

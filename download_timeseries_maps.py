import os
from owslib.wms import WebMapService
wms = WebMapService('https://ec.oceanbrowser.net/emodnet/Python/web/wms', version='1.3.0')

#Chlorophyll Index
#https://ec.oceanbrowser.net/emodnet/Python/web/wms?SERVICE=WMS&REQUEST=GetCapabilities&VERSION=1.3.0

for data in list(wms.contents):
   if "By_sea_regions/Baltic_Sea" in data:
      print(data)

#print(list(wms.contents)) #list all available datasets
#print(dataset.boundingBoxWGS84)
#print([op.name for op in wms.operations])
#print(wms.getOperationByName('GetMap').methods)
#print(wms.getOperationByName('GetMap').formatOptions)
#print(dataset.crsOptions)
#print(dataset.styles)
#print("Dimensions",list(dataset.dimensions)) #Get's time and Elevation 
#Print time and Elevation value
#for keys,values in dataset.dimensions.items():
#    print(keys)
#    print(values)

#Baltic Sea Chlorophyll
dataset = wms['By_sea_regions/Baltic_Sea/Water_body_chlorophyll-a.4Danl.nc*Water body chlorophyll-a_L2']
for time in dataset.dimensions["time"]["values"]:
   time_formatted = time.replace(" ","_")
   out_file_path = f'timeseries/BalticSeaChlorophyll/{time_formatted}.png'
   if os.path.exists(out_file_path):
      continue
   img = wms.getmap(   layers=['By_sea_regions/Baltic_Sea/Water_body_chlorophyll-a.4Danl.nc*Water body chlorophyll-a_L2'],
                       styles=['contourf'],
                       srs='EPSG:4326',
                       bbox=(9.4, 30.9, 53, 65.9),
                       size=(300, 300),
                       time=(time),
                       format='image/png',
                       transparent=True
                    )
   out = open(out_file_path, 'wb')
   out.write(img.read())
   out.close()

dataset = wms['By_sea_regions/Baltic_Sea/Water_body_dissolved_oxygen_concentration.4Danl.nc*Water body dissolved oxygen concentration_L2']
for time in dataset.dimensions["time"]["values"]:
   time_formatted = time.replace(" ","_")
   out_file_path = f'timeseries/BalticSeaOxygen/{time_formatted}.png'
   if os.path.exists(out_file_path):
      continue
   img = wms.getmap(   layers=['By_sea_regions/Baltic_Sea/Water_body_dissolved_oxygen_concentration.4Danl.nc*Water body dissolved oxygen concentration_L2'],
                       styles=['contourf'],
                       srs='EPSG:4326',
                       bbox=(9.4, 30.9, 53, 65.9),
                       size=(300, 300),
                       time=(time),
                       format='image/png',
                       transparent=True
                    )
   out = open(out_file_path, 'wb')
   out.write(img.read())
   out.close()

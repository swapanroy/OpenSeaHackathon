from owslib.wms import WebMapService

wms = WebMapService(url='https://nodc.ogs.it/geoserver/Contaminants/wms', version='1.3.0')

print(wms.identification.type)

print(wms.identification.version)
print(wms.identification.title)
print(wms.identification.abstract)

print(wms.getfeatureinfo)
print(wms.headers)

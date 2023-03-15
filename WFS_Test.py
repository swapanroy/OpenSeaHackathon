from owslib.wfs import WebFeatureService

wfs = WebFeatureService(url='https://ows.emodnet-humanactivities.eu/wfs', version='2.0.0')

print(wfs.identification.title)
print(wfs.identification.abstract)
print(wfs.identification.keywords)



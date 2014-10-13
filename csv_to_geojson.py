import csv
 
# Read in raw data from csv
rawData = csv.reader(open('mass_media.csv', 'r'))
 
# the template. where data from the csv will be formatted to geojson
template = \
    ''' \
    { "type" : "Feature",
	"geometry" : {
                "type" : "Point",
                "coordinates" : [%s, %s]
        },
        "properties" : {
        	"name" : "%s",
        	"location" : "%s",
        	"year" : "%s",
        	"url" : "%s",
        	"address" : "%s",

        	}
        },
    '''


# the head of the geojson file
output = \
    ''' \
{ "type" : "Feature Collection",
    {"features" : [
    '''
 
# loop through the csv by row skipping the first
iter = 0
for row in rawData:
    iter += 1
    if iter >= 2:
        lat = row[5]
        lng = row[6]
        name = row[0]
        location = row[2]
        year = row[1]
        url = row[8]
        address = row[10]

        output += template % (row[5], row[6], row[0], row[2], row[1], row[8], row[10])
         
# the tail of the geojson file
output += \
    ''' \
    ]
}
    '''
     
# opens an geoJSON file to write the output to
outFileHandle = open("output.geojson", "w")
outFileHandle.write(output)
outFileHandle.close()

import json
#opening the file

with open('precipitation.json') as file:
    precipitation = json.load(file)

#filtering out the data for seattle
seattle_data = [0]*12
for measurement in precipitation:
    if measurement['station'] == 'GHCND:US1WAKG0038': #For Seattle station 
       month = int(measurement['date'].split('-')[1]) #this splits the date and only considers the months
       seattle_data[month - 1] += measurement['value'] #from the created list, we now add monthly data

print(seattle_data)

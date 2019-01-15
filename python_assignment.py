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

with open ('seattle_data.json ', 'w') as file: # open JSON file
    json . dump ( seattle_data, file, indent =4, sort_keys = True ) #
#write my_dictionary to file in a pretty JSON format

####PART 2#####

total_precipitation = 0
for i in seattle_data:
    total_precipitation += i

print(total_precipitation)

average = []
for data in seattle_data:
    average.append(data/total_precipitation)

print(average)
import pandas as pd 
import requests
import json
import csv


url = 'http://api.geonames.org/searchJSON?'

#Change df parameters according to excel sheet specification.

df = pd.read_excel('grp.xlsx', sheet_name='Foglio14', usecols="A")

for item in df.place_name:

	df.place_name.head()

	#Change username params with geonames API username

	params ={  	'username': "XXXXXXXX", 
		            
		        'name_equals': item,

		        'maxRows': "1"}

	e = requests.get(url, params=params)

	pretty_json = json.loads(e.text)

	with open("data14.txt", "a") as myfile:

    		writer = csv.writer(myfile)
			                
    		for item in pretty_json["geonames"]:

    				#print("{}, https://www.geonames.org/{}".format(item["name"], item["geonameId"]))

        			writer.writerow([item["name"], "https://www.geonames.org/{}".format(item["geonameId"])])  #Write row.

	myfile.close()
	




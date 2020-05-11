import pandas as pd
import requests
import json
import csv
import numpy as np

API_ENDPOINT = "https://www.wikidata.org/w/api.php"

df = pd.read_excel('place.xlsx', sheet_name='Sheet2')
#print(df)

df1 = (df["UUID"]+ "-" + df["PLACE"])

df2 = df1.astype('str')


for item in df.PLACE:
    df.PLACE.head()
    
    #1st level request
    def wbsearchentities_q(**kwargs):
        params = {
        'action': 'wbsearchentities',
        'format': 'json',
        'language': 'en',
        'search': item
    }        
            
        params.update(kwargs)

        response = requests.get(API_ENDPOINT, params=params)
        return response
    
    r = wbsearchentities_q(ids=item)
    try:
        item_id = (r.json()['search'][0]['id'])
        item_label = (r.json()['search'][0]['label'])    
        

    except IndexError:
        continue 
    
    #2nd level request
    def wbgetentities_q(**kwargs):
        params = {
            'action': 'wbgetentities', 
            'format': 'json'
            }

        params.update(kwargs)

        response = requests.get(API_ENDPOINT, params=params)
        return response

    try:
        resp = wbgetentities_q(ids=item_id)
        resp_obj_str = (resp.json()['entities'][item_id]['claims']['P1566'])
    except KeyError:
        continue
    listString = json.dumps(resp_obj_str)
    
    my_json = json.loads(listString)
    
    for item_label in df2.unique():
        if any(item_label in s for s in df2):
            print(df2)        
            

    try:
        with open("wiki.csv", "a") as myfile:
            writer = csv.writer(myfile)
            for item in my_json:
             writer.writerow([item_label,"https://www.geonames.org/{}".format(item["mainsnak"]["datavalue"]["value"])])
    except KeyError:
        continue
    #myfile.close()

    
    print(resp_obj_str)

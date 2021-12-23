import pandas as pd
# Python program to read
# json file


import json
import csv

f = open('countries.json')
data = json.load(f)
f.close()
array=[]

for key, value in data.items():
  temp = {"Country Name":key,"Number of cities":len(value),"City with max length":max(value, key=len)}
  array.append(temp)


keys = array[0].keys()

with open('result.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(array)




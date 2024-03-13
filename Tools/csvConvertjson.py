import json
import pandas as pd

 # Read the CSV file
csvData = pd.read_csv('csv/datoo.csv')

# Convert CSV data to a list of dictionaries
output = csvData.to_dict(orient='records')

# Save as a JSON file
with open('toto.json', 'w', encoding='utf-8-sig') as jsonFile:
    json.dump(output, jsonFile, ensure_ascii=False, indent=4)
# print(。'')





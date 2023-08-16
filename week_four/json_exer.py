"""
Read and modify a key in the file
change age
"""

import json


with open('person.json', 'r') as json_file:
    json_data = json.load(json_file)
    json_data['age'] = 45


with open('person.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=2)

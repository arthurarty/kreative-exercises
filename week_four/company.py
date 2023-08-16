""""
Read json file and add employee.
"""


import json

JSON_FILE = 'company.json'
with open(JSON_FILE, 'r') as json_file:
    company_data = json.load(json_file)


with open(JSON_FILE, 'w') as json_file:
    employees = company_data['employees']
    employees.append(
        {
            "id": "E003",
            "name": "Jane Doe",
            "position": "Sales Executive"
        }
    )
    json.dump({"employees":employees}, json_file, indent=4)

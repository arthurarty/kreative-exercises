import json


input_data = {
    "name": "John",
    "age": 32
}

print(type(input_data))
print(json.dumps(input_data))
print(type(json.dumps(input_data)))

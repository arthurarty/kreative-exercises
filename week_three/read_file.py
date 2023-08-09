"""
Write a generator function that reads a text file, 
line by line, and returns lines that contain a specific word.
"""


def read_file(file_path: str, query_str: str):
    with open(file_path, 'r') as reader:
        for line in reader.readlines():
            if query_str in line:
                yield line


for desired_line in read_file('sample_text.txt', 'line'):
    print(desired_line)

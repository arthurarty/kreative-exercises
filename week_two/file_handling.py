# file handling
'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists 
'''

'''
"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images) 
'''

f = open("demofile.txt")
print(f)

f = open("demofile.txt", "rt")

# read files
f = open("demofile.txt", "r")
print(f.read())

f = open("demofile.txt", "r")
print(f.read(5))

f = open("romeo.txt", "r")
print(f.readline())

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

f = open("demofile.txt", "r")
for x in f:
  print(x)

f = open("demofile.txt", "r")
print(f.readline())
f.close()

# write/create files
'''
"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content 
'''

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())

''' 
"x" - Create - will create a file, returns an error if the file exist

"a" - Append - will create a file if the specified file does not exist

"w" - Write - will create a file if the specified file does not exist 
'''

# delete files
import os
os.remove("demofile.txt")

if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

os.mkdir("myfolder")


cwd = os.getcwd()
print(cwd)


dir_path = r'C:\Users\F17\Desktop'
files = os.listdir(dir_path)
print(files)

dir_path = r'C:\Users\F17\Desktop\newfile'
os.mkdir(dir_path)


dir_path = r'C:\Users\F17\Desktop'
file_name = 'file.txt'
full_path = os.path.join(dir_path, file_name)

# create the directory if it does not exist
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

# create the file in the directory
with open(full_path, 'w') as f:
    f.write('Hello, world!')


path = '/path/to/dir/file.txt'
basename = os.path.basename(path)
print(basename)


path = '/path/to/dir/file.txt'
dirname = os.path.dirname(path)
print(dirname)



path = '/path/to/dir/file.txt'
dirname, basename = os.path.split(path)
print(dirname, basename)


import shutil

src_file = r'C:\Users\F17\Desktop\test.py'
dst_file = r'C:\Users\F17\Desktop\file.txt'
shutil.copy(src_file, dst_file)


import shutil

src_dir = '/path/to/src_dir'
dst_dir = '/path/to/dst_dir'

shutil.copytree(src_dir, dst_dir)


import shutil

src_file = r'C:\Users\F17\file2.txt'
dst_file = r'C:\Users\F17\Desktop\file.txt'
shutil.move(src_file, dst_file)


import shutil

src_dir = '/path/to/src_dir'
dst_dir = '/path/to/dst_dir'
shutil.move(src_dir, dst_dir)


import shutil

src_dir = r'C:\Users\F17\Desktop'
zip_file = r'C:\Users\F17\Desktop\archive.zip'

shutil.make_archive(zip_file, 'zip', src_dir)


import zipfile

# List of files to include in the ZIP archive
file_list = ['/path/to/file1.txt', '/path/to/file2.txt', '/path/to/file3.txt']

# Name of the output ZIP archive
zip_file = '/path/to/archive.zip'

# Create a new ZIP archive
with zipfile.ZipFile(zip_file, 'w') as archive:
    # Add each file to the archive
    for file in file_list:
        archive.write(file)


# Copy permissions from one file to another
shutil.copystat('/path/to/source/file', '/path/to/destination/file')

# Delete a directory (and its contents)
shutil.rmtree('/path/to/directory')

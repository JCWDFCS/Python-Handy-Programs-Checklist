import os
import glob
# change to the current path
current_path =
'/Users/gaowei/Documents/1.formalScience/3.Computing/1.Python/1.2.murachPython/'
os.chdir(current_path)
# the destination path
destination_path = '/Users/gaowei/Desktop/Murach_Python'
# filter the qualified files
flag_ext = '*.md'
files = glob.glob(path + flag_ext)
# Avoid repeated traverse the directory.
source_files = files[:]
cmd = 'mv %s %s'
for file in source_files:
    os.popen(cmd %(file, destination_path))

import os
import glob
# the current path
path = '/Users/gaowei/Documents/1.formalScience/3.Computing/1.Python/1.2.murachPython/'
os.chdir('/Users/gaowei/Documents/1.formalScience/3.Computing/1.Python/1.2.murachPython/')
# the destination path
destination_path = '/Users/gaowei/Desktop/Murach_Python'
# attain all the qualified files
files = glob.glob(path + '*.py')
# Avoid repeated traverse the directory.
source_files = files[:]
cmd = 'mv %s %s'
for file in source_files:
    os.popen(cmd %(file, destination_path))


import os
import glob

os.chdir('/Users/gaowei/Documents/1.formalScience/3.Computing/1.Python/Murach_Python')
cmd = 'rm %s'
pathnames = glob.glob('ch11*')
for pathname in pathnames:
    os.popen(cmd %pathname)

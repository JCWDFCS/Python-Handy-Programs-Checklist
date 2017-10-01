import os

pathname =  '/Users/gaowei/Desktop' 
os.chdir(pathname)

# Fat Model to manipulate the input to get the entries.
filenames = os.listdir(pathname)
# copy the files
source_filenames = filenames[:]
# print(source_filenames)

for name in source_filenames:
    # if 'F3' in name:
    #     target_name = name[7:]
    #     os.rename(name, target_name)
    # elif 'Python√' in name:
    #     print(name)
    #     os.rename(name, name[7:])
    # elif 'Python·' in name:
    #     print(name)
    #     os.rename(name, name[7:])
    # elif 'Python-' in name:
    #     print(name)
    #     os.rename(name, name[7:])
    if 'Ki' or 'In' or 'Le' in name:
        os.rename(name, name[7:])

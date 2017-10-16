# 1.change to the destination directory
path_name = ' ~/Documents/'
os.chdir(path_name)

# 2.get and validate the '.md' filename
x = os.dirlist(path_name)
qualified_filenames = [i for i in x if '.md' is in x]

# 3.rename '.md' to '.txt'
new_names = []
for i in qualified_filenames:
    name,extension = os.path.splitext(i)
    extension = '.txt'
    new_name = '{}{}'.format(name, extension)
    os.rename(i, new_name)
    new_names.append(new_name)

# 4.read contents from '.txt' to a list
contents_list = []
for i in new_names:
    with open(i) as fp:
        line = fp.read(i)
        contents_list.append(line)

# 5.write to a single '.txt' filename
with open('single-file.txt','w') as fp:
    for i in contents_list:
        fp.write(i + '\n')

# 6.rename the single '.txt' file to '.md'
os.rename('single-file.txt','single-file.md')

# 7.restore all the '.txt' to '.md'
for i, j in zip(new_names, qualified_filenames):
    os.rename(i, j)

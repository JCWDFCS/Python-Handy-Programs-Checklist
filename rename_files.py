import os
import glob

def main():

    pathname = '/Users/gaowei/Documents/myLibrary'
    os.chdir(pathname)

    # Fat Model to manipulate the input to get the entries.
    filenames = os.listdir(pathname)
    # copy the files
    source_filenames = filenames[:]
    # print(source_filenames)

    get_files()
    remove_file()

def rename_file():
    global source_filenames

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

def get_files():
    global pathname
    global files
    filter = '*项目管理*.*'
    files = glob.glob(filter)
    print(files)

def remove_file():
    global files
    dst_dir = '/Users/gaowei/Documents/myLibrary/2.Social-Science/Manage/'

    for file in files:
        dst_f = dst_dir + file[3:]
        print(file[3:])
        os.rename(file, dst_f)


if __name__ == '__main__':
    main()

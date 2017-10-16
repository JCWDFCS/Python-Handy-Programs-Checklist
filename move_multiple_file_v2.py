import os
import glob




# change to the current path,veneer techniques
def change_to_current_directory(src_path):
    os.chdir(src_path)

def filter_files(wildcard_ext,src_path):
    files = glob.glob(src_path + wildcard_ext)
    # Avoid repeated traverse the directory.
    return files[:]


def move_files(wildcard_ext,src_path,dst_path):
     # filter the qualified files
    change_to_current_directory(src_path)
    src_files = filter_files(wildcard_ext,src_path)
    cmd = 'mv %s %s'
    for file in src_files:
        # print the dst path for later manipulating.
        print(dst_path + file[len(src_path):])
        os.popen(cmd %(file, dst_path))

def main():
    # Move images from downloads folder to diary images folers
    download_path =    '/Users/gaowei/Downloads/'
    diary_images_path ='/Users/gaowei/Documents/Diary/images/'
    image_ext =        '*.JPG'
    # move .ext file from src_dir to dst_dir
    move_files(image_ext,download_path,diary_images_path)

if __name__ == '__main__':
    main()

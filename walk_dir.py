import os
# I love recursive


def walk(dirname):
    """Prints the names of all files in dirname and its subdirectories.
    This is the version in the book.
    dirname: string name of directory """
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)


def walk2(dirname):
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            print(os.path.join(root, filename))


if __name__ == '__main__':
    walk('.')
    walk2('.')

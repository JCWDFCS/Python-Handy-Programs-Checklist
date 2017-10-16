


def class_to_dict(cls):
    return {key:cls[key] for key in cls if '__' not in key}




# function `getattr()`
def main():
    class MylibraryDir():
        python = '~/mylibrary/python'
        javacript = '~/mylibrary/javacript'
        def __init__(self):
            def jump_around(self):
                pass

    a = MylibraryDir

    class_to_dict(a)

if __name__ == '__main__':
    main()


    # >>> cls = dict(vars(Mylibrary))
    # >>> {key:cls[key] for key in cls if '__' not in key}
    # {'html': '/Users/gaowei/Documents/myLibrary/1.2.Computing/HTML', 'base': '/Users/gaowei/Documents/myLibrary', 'language': '/Users/gaowei/Documents/myLibrary/2.Social-Science/Language', 'psychology': '/Users/gaowei/Documents/myLibrary/2.Social-Science/Psychology'}

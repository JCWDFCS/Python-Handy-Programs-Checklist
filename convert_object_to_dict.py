


def class_to_dict(cls):
    my_dict = dict(vars(cls))
    return {key:my_dict[key] for key in my_dict if '__' not in key}




# function `getattr()`
def main():
class MylibraryDir():
    def __init__(self):
        self.python = '~/mylibrary/python'
        self.javacript = '~/mylibrary/javacript'
    def jump_around(self):
        return self.python + self.javacript

    a = MylibraryDir

    class_to_dict(a)

if __name__ == '__main__':
    main()


    # >>> cls = dict(vars(Mylibrary))
    # >>> {key:cls[key] for key in cls if '__' not in key}
    # {'html': '/Users/gaowei/Documents/myLibrary/1.2.Computing/HTML', 'base': '/Users/gaowei/Documents/myLibrary', 'language': '/Users/gaowei/Documents/myLibrary/2.Social-Science/Language', 'psychology': '/Users/gaowei/Documents/myLibrary/2.Social-Science/Psychology'}

class Test:
    def __init__(self):
        self.varOne = ""
        self.varTwo = ""
        self.varThree = ""
    def methodOne(self):
        print ("You just called methodOne!")


if __name__ == "__main__":
    t = Test()

    class Book(object):
        def __init__(self, title, author):
            self.title = title
            self.author = author

        def get_entry(self):
            return "{} by {} on {}".format(self.title, self.author, self.pubyear)

        entry = property(get_entry)


class NewClass:
    def __init__(self,number):
        self.multi = int(number) * 2
        self.str   = str(number)
